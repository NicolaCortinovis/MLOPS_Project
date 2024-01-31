from ConversationSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ConversationSummarizer.logging import logger

STAGE = "Data ingestion stage"

try:
    logger.info(f"@@@@@@@@@@@@ Starting {STAGE} @@@@@@@@@@@@")
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main()
    logger.info(f"@@@@@@@@@@@@ Completed {STAGE} @@@@@@@@@@@@")
except Exception as e:
    logger.exception(f"{STAGE} failed with the following exception: {e}")
    raise 