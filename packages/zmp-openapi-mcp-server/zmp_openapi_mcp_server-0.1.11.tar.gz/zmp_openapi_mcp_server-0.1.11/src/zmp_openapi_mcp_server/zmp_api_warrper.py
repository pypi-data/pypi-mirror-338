from zmp_openapi_toolkit import AuthenticationType, MixedAPISpecConfig, ZmpAPIWrapper

import logging

logger = logging.getLogger(__name__)


def get_zmp_api_wrapper(endpoint: str, access_key: str, spec_path: str):
    logger.info(f":::: endpoint: {endpoint}")
    logger.info(f":::: access_key: {access_key}")
    logger.info(f":::: spec_path: {spec_path}")

    try:
        mixed_api_spec_config = MixedAPISpecConfig.from_mixed_spec_file(
            file_path=spec_path
        )
    except Exception as e:
        raise ValueError(f"Failed to load OpenAPI spec file: {e}")

    zmp_api_wrapper = ZmpAPIWrapper(
        endpoint,
        auth_type=AuthenticationType.ACCESS_KEY,
        access_key=access_key,
        mixed_api_spec_config=mixed_api_spec_config,
    )

    operations = zmp_api_wrapper.get_operations()

    for operation in operations:
        logger.debug("-" * 100)
        logger.debug(f"args_schema: {operation.args_schema.model_json_schema()}")


    return zmp_api_wrapper