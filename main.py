from mlopsProject.logging import logger
from mlopsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlopsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"############# Starting execution of {STAGE_NAME} #############")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"############# Finished execution of {STAGE_NAME} #############")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data validation stage"

try:
    logger.info(f"############# Starting execution of {STAGE_NAME} #############")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"############# Finished execution of {STAGE_NAME} #############")
except Exception as e:
    logger.exception(e)
    raise e
