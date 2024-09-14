import warnings
from model.model_service import ModelService
from loguru import logger
from config.logger import configure_logging

configure_logging='DEBUG'


warnings.filterwarnings("ignore", message="X does not have valid feature names")
@logger.catch
def main():
    logger.info("Runnig the application")
    # test
    ml_srv=ModelService()
    ml_srv.load_model()
    pred=ml_srv.predict([200, 2024, 2, 20, 1, 2, 3, 4, 1])
    logger.info(pred)
    
if __name__=='__main__':
    main()
