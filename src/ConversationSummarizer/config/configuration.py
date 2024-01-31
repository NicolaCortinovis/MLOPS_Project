from ConversationSummarizer.constants import *
from ConversationSummarizer.utils.common import read_yaml, create_directories
from ConversationSummarizer.entity import DataIngestionConfig

# Define a class for managing configurations
class ConfigurationManager:
    # Initialize the ConfigurationManager with paths to the configuration and parameters files
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        # Read the configuration and parameters files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create the root directory for storing artifacts
        create_directories([self.config.artifacts_root])
        
    # Define a method for getting the data ingestion configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        # Get the data ingestion configuration from the config file
        config = self.config.data_ingestion 
        
        # Create the root directory for data ingestion, if it doesn't already exist
        create_directories([config.root_dir])
        
        # Create a DataIngestionConfig object with the configuration values
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        # Return the DataIngestionConfig object
        return data_ingestion_config