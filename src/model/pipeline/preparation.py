from model.pipeline.collection import load_data_from_db
import pandas as pd
import re
from loguru import logger

def prepare_data():
    logger.info("starting up prepossing pipeline")
# To prepare the dataset we  need:
 
# load the dataset
    data = load_data_from_db()
# encode columns like balcony,parking,etc
    data_encoded=encode_cat_cols(data)
# parse the garden column   
    df = parse_garden_col(data_encoded)
    
    return df

def encode_cat_cols(df):
     cols= ["balcony", "storage", "parking", "furnished", "garage"]
     logger.info(f"encoding categorical columns: {cols}")
     return pd.get_dummies(df, columns=cols , drop_first=True)
     
def parse_garden_col(data):
    logger.info("parsing garden column")
    for i in range(len(data)):
        if data.loc[i, 'garden'] == "Not Present":
            data.loc[i, 'garden'] = 0
        elif isinstance(data.loc[i, 'garden'], str):
        # Find all digits in the string
            digits = re.findall(r'\d+', data.loc[i, 'garden'])
        # Check if the list is not empty
        if digits:
            data.loc[i, 'garden'] = int(digits[0])
        else:
            # Handle cases where no digits are found
            data.loc[i, 'garden'] = 0
    return data

