from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path  # The root directory where the data will be stored
    source_URL : str  # The URL of the source data
    local_data_file : Path  # The path of the local file where the data will be downloaded
    unzip_dir : Path  # The directory where the data file will be unzipped