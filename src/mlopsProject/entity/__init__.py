from dataclasses import dataclass 
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path 
    unzip_dir : Path

@dataclass(frozen = True)
class DataValidationConfig:
    root_dir : Path 
    STATUS_FILE : str 
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir : Path 
    data_path : Path 
    tokenizer_name : str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path 
    data_path : Path 
    model_ckpt : str 
    num_train_epochs : int
    warmup_steps : int 
    per_device_train_batch_size : int
    per_device_eval_batch_size : int
    weight_decay : float 
    logging_steps : int
    evaluation_strategy : str 
    eval_steps : int 
    gradient_accumulation_steps : int
    predict_with_generate : bool 
    eval_dataset_dimension : int 
