from ConversationSummarizer.config.configuration import ConfigurationManager
from ConversationSummarizer.components.model_evaluation import ModelEvaluation
from ConversationSummarizer.logging import logger




class ModelEvaluationTrainingPipeline:
    """
    This class represents the training pipeline for model evaluation.
    """

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()