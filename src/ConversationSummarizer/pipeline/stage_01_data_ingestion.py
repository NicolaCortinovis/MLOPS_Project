from ConversationSummarizer.config.configuration import ConfigurationManager
from ConversationSummarizer.components.data_ingestion import DataIngestion
from ConversationSummarizer.logging import logger


class DataIngestionTrainingPipeline():
    
    def __init__(self):
        pass

    def main(self):
        # Instantiate ConfigurationManager and get the data ingestion configuration
        config = ConfigurationManager() 
        data_ingestion_config = config.get_data_ingestion_config()

        # Instantiate DataIngestion with the configuration and perform data ingestion
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()