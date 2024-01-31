from pathlib import Path

# Define the path to the configuration file
CONFIG_FILE_PATH = Path("config/config.yaml")

# Define the path to the parameters file
PARAMS_FILE_PATH = Path("params.yaml")

# Maximum length for the input sequences. Any input sequence longer than this will be truncated.
MAX_INPUT_LENGTH = 1024

# Maximum length for the target sequences. Any target sequence longer than this will be truncated.
MAX_TARGET_LENGTH = 128
