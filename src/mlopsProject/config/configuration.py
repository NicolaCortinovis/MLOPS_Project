from mlopsProject.constants import *
from mlopsProject.utils.common import read_yaml, create_directory
from mlopsProject.entity import DataIngestionConfig, DataValidationConfig, DataPreprocessingConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):

            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion 

        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        
        config = self.config.data_validation

        create_directory([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        
        config = self.config.data_preprocessing

        create_directory([config.root_dir])

        data_preprocessing_config = DataPreprocessingConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_preprocessing_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directory([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps,
            per_device_eval_batch_size = params.per_device_eval_batch_size,
            predict_with_generate = params.predict_with_generate,
            eval_dataset_dimension = params.eval_dataset_dimension
        )

        return model_trainer_config