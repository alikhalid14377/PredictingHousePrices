#1 pick up model
    #1.1 if model file exist, load the trained model
    #1.2 if not exits -> train model to get it
#2 make predictions

from pathlib import Path
import pickle as pk
from model.pipeline.model import build_model
from config import model_settings
from loguru import logger

class ModelService():
    def __init__(self):
        self.model=None
        
    def load_model(self):
        logger.info(f"Checking the existance of model config file at {model_settings.model_path}/{model_settings.model_name}")
        model_path=Path(f'{model_settings.model_path}/{model_settings.model_name}')
        
        if not model_path.exists():
            logger.warning(f"Model not found at {model_settings.model_path}/{model_settings.model_name} -> building the model {model_settings.model_name}")
            build_model()
            
        self.model= pk.load(open(f'{model_settings.model_path}/{model_settings.model_name}', 'rb'))
        
    def predict(self, input_parameters):
        logger.info("Making prediction!!")
        return self.model.predict([input_parameters])
    

        