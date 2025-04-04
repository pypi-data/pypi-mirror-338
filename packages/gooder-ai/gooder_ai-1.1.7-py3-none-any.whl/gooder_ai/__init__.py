from datetime import datetime
from uuid import uuid4
from webbrowser import open_new
from gooder_ai.globals import Amplify_Env
from gooder_ai.s3 import upload_files
from gooder_ai.view import execute_graphql_query, ExecuteGraphQLParams
from gooder_ai.auth import authenticate
from gooder_ai.utils import (
    validate_config,
    get_transformed_data,
    get_score_column_names,
    get_scorer_functions,
    save_config,
    get_positive_class,
)
from gooder_ai.types import (
    ViewMeta,
    ValuateModelOutput,
    ScikitModel,
    Credentials,
    AWSVariables,
    ColumnNames,
    Data,
)
from asyncio import to_thread
from pandas import DataFrame, concat
import logging
import os


async def valuate_model(
    models: list[ScikitModel],
    x_data: Data,
    y: Data,
    auth_credentials: Credentials,
    config: dict,
    view_meta: ViewMeta,
    scorer_names: list[str] = [],
    column_names: ColumnNames = {},
    filtered_columns: list[str] = [],
    aws_variables: AWSVariables = {},
    upload_data_to_gooder: bool = True,
    upload_config_to_gooder: bool = True,
    amplify_env: str = "seventeen",  # For production the amplify version is seventeen
    max_size: int = 10,
) -> ValuateModelOutput:
    logging.info("Model valuation started.")
    email = auth_credentials["email"]
    password = auth_credentials["password"]
    mode = view_meta.get("mode", "private")
    view_id = view_meta.get("view_id", None)
    dataset_name = view_meta.get("dataset_name", f"{datetime.now().timestamp()}")
    # Create a copy of the config to avoid modifying the original
    raw_config = {**config}

    # AWS Global Variables
    api_url = aws_variables.get("api_url", Amplify_Env[amplify_env]["API_URL"])
    app_client_id = aws_variables.get(
        "app_client_id", Amplify_Env[amplify_env]["App_Client_ID"]
    )
    identity_pool_id = aws_variables.get(
        "identity_pool_id", Amplify_Env[amplify_env]["Identity_Pool_ID"]
    )
    user_pool_id = aws_variables.get(
        "user_pool_id", Amplify_Env[amplify_env]["User_Pool_ID"]
    )
    bucket_name = aws_variables.get(
        "bucket_name", Amplify_Env[amplify_env]["Bucket_Name"]
    )
    base_url = aws_variables.get("base_url", Amplify_Env[amplify_env]["Base_URL"])
    validation_api_url = aws_variables.get(
        "validation_api_url", Amplify_Env[amplify_env]["Validation_API_URL"]
    )

    transformed_x_data = get_transformed_data(
        x_data, column_names.get("dataset_column_names", [])
    )

    filtered_x_data = (
        transformed_x_data.filter(items=filtered_columns)
        if len(filtered_columns) > 0
        else transformed_x_data
    )

    transformed_y_data = get_transformed_data(
        y, [column_names.get("dependent_variable_name", "dependent_variable")]
    )

    combined_dataframe = concat([filtered_x_data, transformed_y_data], axis=1)

    # Ref: https://stackoverflow.com/questions/18089667/how-to-estimate-how-much-memory-a-pandas-dataframe-will-need
    # Ref: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#
    df_memory = combined_dataframe.memory_usage(deep=True).sum() / (
        1024 * 1024
    )  # Convert into MB

    if df_memory >= max_size:
        logging.error(
            "Failed: Provided DataFrame size exceeding the maximum allowed limit."
        )
        raise Exception(
            "Provided DataFrame size is exceeding the maximum allowed limit. Please reduce the size of the DataFrame."
        )

    scorer_functions = get_scorer_functions(len(models), scorer_names)

    for index, model in enumerate(models):
        scorer = getattr(model, scorer_functions[index])
        # Ref: https://stackoverflow.com/questions/52763325/how-to-obtain-only-the-name-of-a-models-object-in-scikitlearn
        model_name = type(model).__name__
        if scorer is None:
            logging.error(
                f"Failed: Input model instance doesn't have a '{scorer_functions[index]}' method to score the model performance."
            )
            raise Exception(
                f"Failed: Input model instance doesn't have a '{scorer_functions[index]}' method to score the model performance."
            )
        model_classes = getattr(model, "classes_", None)
        if model_classes is None:
            logging.error(
                "Failed: Input model instance doesn't have classes to classify the target variable"
            )
            raise Exception(
                "Failed: Input model instance doesn't have classes to classify the target variable."
            )
        score_column_names = get_score_column_names(
            {
                "column_names": column_names.get("score_column_names", []),
                "scores": model_classes,
                "model_name": f"{model_name}-{index}",
            }
        )

        full_scores_df = DataFrame(
            scorer(x_data), columns=score_column_names, index=combined_dataframe.index
        )

        if len(model_classes) == 2:
            # handle binary classification
            positive_class = get_positive_class(transformed_y_data)
            positive_class_index = list(model_classes).index(positive_class)
            new_score_entry = {"fieldName": f"{model_name}-{index}"}
            logging.info(f"Creating new score entry: {new_score_entry}")

            positive_class_score_name = score_column_names[positive_class_index]
            full_scores_df = full_scores_df[[positive_class_score_name]].rename(
                columns={positive_class_score_name: f"{model_name}-{index}"}
            )

            raw_config["scores"] = raw_config.get("scores", []) + [new_score_entry]
            logging.info(
                f"Updated config scores in binary classification: {raw_config['scores']}"
            )
        else:
            # handle multi-class classification
            raw_config["scores"] = raw_config.get("scores", []) + score_column_names
            logging.info(
                f"Updated config scores in multi-class classification: {raw_config['scores']}"
            )

        combined_dataframe = concat(
            [
                combined_dataframe,
                full_scores_df,
            ],
            axis=1,
        )

    df_memory = combined_dataframe.memory_usage(deep=True).sum() / (
        1024 * 1024
    )  # Recalculate the DataFrame size in MB after performing calculations

    if df_memory >= max_size:
        logging.error(
            "Failed: Provided DataFrame size exceeding the maximum allowed limit."
        )
        raise Exception(
            "Provided DataFrame size is exceeding the maximum allowed limit. Please reduce the size of the DataFrame."
        )

    logging.info("Started: Validating config as per the Gooder AI schema.")
    parsed_config = await validate_config(validation_api_url, raw_config)

    if parsed_config["success"] == False:
        logging.error("Failed: Validating config as per the Gooder AI schema.")
        raise Exception("Invalid configuration", parsed_config["error"])
    else:
        logging.info("Success: Validating config as per the Gooder AI schema.")

    logging.info("Started: Authenticating for the Gooder AI platform.")
    credentials = authenticate(
        {
            "email": email,
            "password": password,
            "app_client_id": app_client_id,
            "identity_pool_id": identity_pool_id,
            "user_pool_id": user_pool_id,
        }
    )
    logging.info("Success: Authenticating for the Gooder AI platform.")

    token = credentials["cognito_client_response"]["AuthenticationResult"][
        "AccessToken"
    ]
    aws_access_key_id = credentials["cognito_credentials"]["Credentials"]["AccessKeyId"]
    aws_secret_access_key = credentials["cognito_credentials"]["Credentials"][
        "SecretKey"
    ]
    aws_session_token = credentials["cognito_credentials"]["Credentials"][
        "SessionToken"
    ]
    identity_id = credentials["cognito_credentials"]["IdentityId"]

    parsed_config["data"][
        "datasetID"
    ] = f"{dataset_name}.csv/Sheet1"  # override datasetID of config to match with dataset.

    if upload_data_to_gooder == True:
        logging.info("Started: Uploading dataset to the Gooder AI platform.")

    if upload_config_to_gooder == True:
        logging.info("Started: Uploading config to the Gooder AI platform.")

    path_dictionary = await upload_files(
        {
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key,
            "aws_session_token": aws_session_token,
            "identity_id": identity_id,
            "data": combined_dataframe,
            "config": parsed_config["data"],
            "file_name": dataset_name,
            "mode": mode,
            "bucket_name": bucket_name,
            "upload_data_to_gooder": upload_data_to_gooder,
            "upload_config_to_gooder": upload_config_to_gooder,
        }
    )
    csv_path = path_dictionary["csv_path"]
    config_path = path_dictionary["config_path"]

    if csv_path is None and upload_data_to_gooder == True:
        logging.error("Failed: Uploading dataset to the Gooder AI platform.")
        raise Exception("Failed to upload dataset")
    elif upload_data_to_gooder == False:
        local_dataset_filename = f"{dataset_name}.csv"
        # Ref: https://docs.python.org/3/library/asyncio-task.html#running-in-threads
        # TODO: Do we need to_thread ?
        await to_thread(
            lambda: combined_dataframe.to_csv(local_dataset_filename, index=False)
        )
        logging.info(f"Dataset saved as {os.path.abspath(local_dataset_filename)}.")

    if config_path is None and upload_config_to_gooder == True:
        logging.error("Failed: Uploading config to the Gooder AI platform.")
        raise Exception("Failed to upload config")
    elif upload_config_to_gooder == False:
        local_config_filename = (
            f"{dataset_name}.json"  # JSON file name is same as dataset_name file name
        )
        # Ref: https://docs.python.org/3/library/asyncio-task.html#running-in-threads
        # TODO: Do we need to_thread ?
        await to_thread(
            lambda: save_config(parsed_config["data"], local_config_filename)
        )
        logging.info(f"Config saved as {os.path.abspath(local_config_filename)}.")

    mutation_type = (
        "updateSharedView" if isinstance(view_id, str) else "createSharedView"
    )
    view_params: ExecuteGraphQLParams = {
        "api_url": api_url,
        "token": token,
        "mutation": mutation_type,
        "variables": {
            "input": {
                "configPath": config_path,
                "datasetPath": csv_path,
                "id": view_id if isinstance(view_id, str) else f"{uuid4()}",
            }
        },
    }

    id: str | None = None
    if upload_config_to_gooder == True or upload_data_to_gooder == True:
        view = await execute_graphql_query(view_params)
        id = view["data"][mutation_type]["id"]
        message = (
            f"View with ID {id} has been successfully updated using the provided view ID: {view_id}."
            if mutation_type == "updateSharedView"
            else f"A new view has been created successfully. Your view ID is {id}. Please save it for future reference and reuse."
        )
        logging.info(message)
        logging.info("Model valuation can be continued on the Gooder AI platform now.")

    view_url = base_url if id is None else f"{base_url}?view={id}"
    open_new(view_url)
    return {"view_id": id, "view_url": view_url}
