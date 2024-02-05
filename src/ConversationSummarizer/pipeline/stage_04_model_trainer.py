from ConversationSummarizer.config.configuration import ConfigurationManager
from ConversationSummarizer.components.model_trainer import ModelTrainer
from ConversationSummarizer.logging import logger


class ModelTrainerTrainingPipeline:
    """
    Class representing the training pipeline for the model trainer.
    """

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()