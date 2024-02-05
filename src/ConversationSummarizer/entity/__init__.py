from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path  # The root directory where the data will be stored
    source_URL : str  # The URL of the source data
    local_data_file : Path  # The path of the local file where the data will be downloaded
    unzip_dir : Path  # The directory where the data file will be unzipped
    
@dataclass(frozen = True)
class DataValidationConfig:
    root_dir : Path # The root directory for data validation
    STATUS_FILE : str  # Status file to check if data validation was successful
    ALL_REQUIRED_FILES : list # List of all required files

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir : Path  # The root directory where data transformation artifacts will be stored
    data_path : Path  # The path to the dataset that will be transformed
    tokenizer_name : str  # The name of the tokenizer that will be used to transform the data
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path              # The root directory where the model and data are stored
    data_path: Path             # The path to the data for training and evaluation
    model_ckpt: Path            # The path to the model checkpoint
    num_train_epochs: int       # The number of epochs for training
    warmup_steps: int           # The number of steps for the warmup phase
    per_device_train_batch_size: int  # The batch size for training per device
    per_device_eval_batch_size: int   # The batch size for evaluation per device
    weight_decay: float         # The weight decay for the optimizer
    logging_steps: int          # The number of steps between each logging
    evaluation_strategy: str    # The strategy to use for evaluation
    eval_steps: int             # The number of steps between each evaluation
    save_steps: int             # The number of steps between each model saving
    gradient_accumulation_steps: int  # The number of steps to accumulate gradients before performing an optimization step


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path  # The root directory where the model and data are stored
    data_path: Path  # The path to the data for evaluation
    model_path: Path  # The path to the trained model
    tokenizer_path: Path  # The path to the tokenizer used in the model
    metric_file_name: Path  # The name of the file where the evaluation metrics will be stored