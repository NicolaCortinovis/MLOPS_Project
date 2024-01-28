from mlopsProject.config.configuration import ConfigurationManager
from mlopsProject.components.data_ingestion import DataIngestion
from mlopsProject.logging import logger

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass 

    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()
        data_ingestion.delete_local()