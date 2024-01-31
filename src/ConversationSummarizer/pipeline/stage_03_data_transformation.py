from ConversationSummarizer.config.configuration import ConfigurationManager
from ConversationSummarizer.components.data_transformation import DataTransformation
from ConversationSummarizer.logging import logger


class DataTrasformationTrainingPipeline():
    
    def __init__(self):
        pass

    def main(self):
        # Instantiate ConfigurationManager and get the data transformation configuration
        config = ConfigurationManager() 
        data_transformation_config = config.get_data_transformation_config()

        # Instantiate DataTransformation with the configuration and perform data transformation
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()