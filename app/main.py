from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    logger.error(f"Failed to execute {STAGE_NAME}")
    raise e