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
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path