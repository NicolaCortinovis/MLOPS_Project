import os
from ConversationSummarizer.logging import logger
from ConversationSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exists(self) -> bool:
        try:
            # Get the list of all files in the specified directory
            all_files = os.listdir((os.path.join("artifacts","data_ingestion","samsum_dataset")))

            # Check if all required files are present
            missing_files = [file for file in self.config.ALL_REQUIRED_FILES if file not in all_files]

            # If there are missing files, validation fails
            validation_status = len(missing_files) == 0

            # Write the validation status to the status file
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            # Log the error message and the stack trace
            logger.error(f"An error occurred during file validation: {e}", exc_info=True)
            raise
        