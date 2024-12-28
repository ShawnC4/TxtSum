from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logging import logger
from src.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
        
    def main(self):
        config_manager = ConfigurationManager()
        config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(config)
        model_trainer.train()