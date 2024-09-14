from pydantic_settings import BaseSettings
from sqlalchemy import create_engine

class DbSettings(BaseSettings):
    db_con:str
    rent_apart_table_name:str
    
    class Config:
        env_file = 'config/.env'  # Path to the .env file
        env_file_encoding = 'utf-8'  # Encoding for the .env file    
        protected_namespaces = ("settings_",)  # Protect the 'settings_' namespace
        extra='ignore'
        extra='allow'
            
db_settings = DbSettings()
    
engine=create_engine(db_settings.db_con)   
    