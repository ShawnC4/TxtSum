import os
from src.logging import logger
from src.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_all_files_exist(self):
        try:
            validation_status = True
            all_files = os.listdir(os.path.join("app", "artifacts", "data_ingestion", "samsum_dataset"))
            missing_files = []
            invalid_files = []
            
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False
                    missing_files.append(required_file)
                    logger.error(f"{required_file} exists: Failed")
                else:
                    logger.info(f"{required_file} exists: Passed")
                    file_path = os.path.join("app", "artifacts", "data_ingestion", "samsum_dataset", required_file)
                    # Check if the required file is a directory
                    if os.path.isdir(file_path):
                        # Check for .arrow files within the directory
                        arrow_files = [f for f in os.listdir(file_path) if f.endswith('.arrow')]
                        if not arrow_files:
                            validation_status = False
                            invalid_files.append(f"{required_file} (no .arrow files found)")
                            logger.error(f".arrow files exists in {required_file}: Failed")
                        else:
                            logger.info(f".arrow files exists in {required_file}: Passed")
                            for arrow_file in arrow_files:
                                arrow_file_path = os.path.join(file_path, arrow_file)
                                # Check file size (example: file should not be empty)
                                if os.path.getsize(arrow_file_path) == 0:
                                    validation_status = False
                                    invalid_files.append(f"{arrow_file} (empty file)")
                                    logger.error(f"arrow file not empty: Failed")
                                else:
                                    logger.info(f"arrow file not empty: Passed")
                    else:
                        # Check file size (example: file should not be empty)
                        if os.path.getsize(file_path) == 0:
                            validation_status = False
                            invalid_files.append(f"{required_file} (empty file)")
                            

            # Write validation status to the status file
            with open(self.config.STATUS_FILE, "w") as f:
                if validation_status:
                    f.write("Validation Status: True\n")
                else:
                    f.write(f"Validation Status: {validation_status}\n")
                    if missing_files:
                        f.write(f"Missing Files: {', '.join(missing_files)}\n")
                    if invalid_files:
                        f.write(f"Invalid Files: {', '.join(invalid_files)}\n")

            return validation_status
        except Exception as e:
            raise e