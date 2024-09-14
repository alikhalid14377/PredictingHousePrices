# from pydantic_settings import BaseSettings, SettingsConfigDict
# from loguru import logger
# from typing import ClassVar

# class LoggerSettings(BaseSettings):
#     log_level:str
    
#     model_Config:ClassVar[dict]={
#         'env_file': 'config/.env' , # Path to the .env file
#         'env_file_encoding': 'utf-8',  # Encoding for the .env file    
#         'protected_namespaces': ('settings_', 'model_'), # Protect the 'settings_' namespace
#         'extra':'ignore'}

# def configure_logging(log_level):
    
#     logger.remove()
#     logger.add('logs/app.log',
#             rotation="1 day",
#             retention="2 day",
#             compression="zip",
#             level=log_level,
#             diagnose=True,
#             )
# configure_logging(log_level=LoggerSettings().log_level) 
from loguru import logger
from pydantic_settings import BaseSettings

class LoggerSettings(BaseSettings):
    log_level: str

    class Config:
        env_file = 'config/.env'
        env_file_encoding = 'utf-8'
        extra = 'ignore'

def configure_logging(log_level: str):
    """Configures the Loguru logger based on the provided log level."""
    logger.remove()  # Remove default logger configuration
    logger.add('logs/app.log', rotation="1 day", retention="2 day", compression="zip", level=log_level)
    logger.info(f"Logger initialized with level: {log_level}")

# Instantiate settings to configure logging
settings = LoggerSettings()
configure_logging(settings.log_level)
