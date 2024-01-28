from mlopsProject.config.configuration import ConfigurationManager
from mlopsProject.components.data_preprocessing import DataPreprocessing
from mlopsProject.logging import logger

class DataPreprocessingTrainingPipeline:

    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config = data_preprocessing_config)
        data_preprocessing.create_DatasetDict()
        data_preprocessing.process()
