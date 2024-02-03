from ConversationSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ConversationSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ConversationSummarizer.pipeline.stage_03_data_transformation import DataTrasformationTrainingPipeline
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

STAGE = "Data validation stage"

try:
    logger.info(f"@@@@@@@@@@@@ Starting {STAGE} @@@@@@@@@@@@")
    data_validation = DataValidationTrainingPipeline() 
    data_validation.main()
    logger.info(f"@@@@@@@@@@@@ Completed {STAGE} @@@@@@@@@@@@")
except Exception as e:
    logger.exception(f"{STAGE} failed with the following exception: {e}")
    raise

STAGE = "Data transformation stage"

try:
    logger.info(f"@@@@@@@@@@@@ Starting {STAGE} @@@@@@@@@@@@")
    data_transformation = DataTrasformationTrainingPipeline() 
    data_transformation.main()
    logger.info(f"@@@@@@@@@@@@ Completed {STAGE} @@@@@@@@@@@@")
except Exception as e:
    logger.exception(f"{STAGE} failed with the following exception: {e}")
    raise

STAGE_NAME = "Model Trainer stage"
try: 
    logger.info(f"@@@@@@@@@@@@ Completed {STAGE} @@@@@@@@@@@@")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"@@@@@@@@@@@@ Completed {STAGE} @@@@@@@@@@@@")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation stage"
try: 
    logger.info(f"@@@@@@@@@@@@ Starting {STAGE} @@@@@@@@@@@@")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"@@@@@@@@@@@@ Completed {STAGE} @@@@@@@@@@@@")
except Exception as e:
        logger.exception(e)
        raise e