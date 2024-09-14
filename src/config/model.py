# data_file_name - path to our csv file in collection.py 
# model_path - the folder containing model config files
# model_name - the name of the model we should use

from pydantic_settings import BaseSettings
from pydantic import DirectoryPath


class ModelSettings(BaseSettings):
    model_path: DirectoryPath
    model_name: str
  
    
    class Config:
        env_file = 'config/.env'  # Path to the .env file
        env_file_encoding = 'utf-8'  # Encoding for the .env file    
        protected_namespaces = ("settings_",)  # Protect the 'settings_' namespace
        extra='ignore'
        extra='allow'

   
model_settings = ModelSettings()

  
    