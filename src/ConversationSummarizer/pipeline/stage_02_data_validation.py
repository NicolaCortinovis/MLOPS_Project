from ConversationSummarizer.config.configuration import ConfigurationManager
from ConversationSummarizer.components.data_validation import DataValidation
from ConversationSummarizer.logging import logger


class DataValidationTrainingPipeline():
    
    def __init__(self):
        pass

    def main(self):
        # Instantiate ConfigurationManager and get the data validation configuration
        config = ConfigurationManager() 
        data_validation_config = config.get_data_validation_config()

        # Instantiate DataValidation with the configuration and perform data validation
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files_exists()