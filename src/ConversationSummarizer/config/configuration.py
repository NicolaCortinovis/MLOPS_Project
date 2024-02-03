from ConversationSummarizer.constants import *
from ConversationSummarizer.utils.common import read_yaml, create_directories
from ConversationSummarizer.entity import DataIngestionConfig
from ConversationSummarizer.entity import DataValidationConfig
from ConversationSummarizer.entity import DataTransformationConfig

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

# Define a method for getting the data validation configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        
        # Get the data validation configuration from the config file
        config = self.config.data_validation
        
        # Create the root directory for data validation, if it doesn't already exist
        create_directories([config.root_dir])
        
        # Create a DataIngestionConfig object with the configuration values
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )
        
        # Return the DataValidationConfig object
        return data_validation_config

# Define a method for getting the data transformation configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        
        # Get the data transformation configuration from the config file
        config = self.config.data_transformation
        
        # Create the root directory for data transformation, if it doesn't already exist
        create_directories([config.root_dir])
        
        # Create a DataTransformationConfig object with the configuration values
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )
        
        # Return the DataTransformationConfig object
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
            """
            Retrieves the configuration for the model trainer.

            Returns:
                ModelTrainerConfig: The configuration for the model trainer.
            """
            config = self.config.model_trainer
            params = self.params.TrainingArguments

            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_ckpt = config.model_ckpt,
                num_train_epochs = params.num_train_epochs,
                warmup_steps = params.warmup_steps,
                per_device_train_batch_size = params.per_device_train_batch_size,
                weight_decay = params.weight_decay,
                logging_steps = params.logging_steps,
                evaluation_strategy = params.evaluation_strategy,
                eval_steps = params.evaluation_strategy,
                save_steps = params.save_steps,
                gradient_accumulation_steps = params.gradient_accumulation_steps
            )

            return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
            """
            Returns the configuration for model evaluation.

            Returns:
                ModelEvaluationConfig: The configuration for model evaluation.
            """
            config = self.config.model_evaluation

            create_directories([config.root_dir])

            model_evaluation_config = ModelEvaluationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                model_path = config.model_path,
                tokenizer_path = config.tokenizer_path,
                metric_file_name = config.metric_file_name
               
            )

            return model_evaluation_config
