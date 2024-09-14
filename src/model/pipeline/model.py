import pickle as pk
from model.pipeline.preparation import prepare_data
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from config import model_settings
from loguru import logger

def build_model():
    logger.info("staring up building the model pipeline")

    # To train and then save the model we need:

    #1 load preprocessed dataset
    df = prepare_data()
    #2 identify x and y
    X,y= get_X_y(df)
    #3 split the dataset
    X_train, X_test, y_train, y_test=split_data(X,y)
    #4 train the model
    rf= train_model(X_train, y_train)
    #5 evaluate the model
    model_evaluate(rf, X_test, y_test)
    #6 save the model in the configeration file
    save_model(rf)
    

def get_X_y(data,
            col_X=["area",
                    "constraction_year",
                    "bedrooms",
                     "garden",
                     "balcony_yes",
                     "parking_yes",
                     "furnished_yes",
                     "garage_yes",
                     "storage_yes"],
            col_y='rent'):
    logger.info("Defining X and y variables.\n X vars: {col_X} \n y vars: {col_y}")
    return data[col_X], data[col_y]

def split_data(X,y):
    logger.info("Splitting data into train and test sets")
    X_train, X_test, y_train, y_test=train_test_split (X,
                                                       y,
                                                       test_size=0.2)
    return X_train, X_test, y_train, y_test

def train_model(X_train,y_train):
    logger.info("Training a model with hyperparameters")
    grid_space={"n_estimators":[100,200,300],
                "max_depth":[3,6,9,12]}
    
    logger.debug(f"Grid space = {grid_space}")
    grid= GridSearchCV(RandomForestRegressor()
                   ,param_grid=grid_space,
                    cv=5,
                    scoring='r2')
    
    model_grid=grid.fit(X_train,y_train)

    
    return model_grid.best_estimator_

def model_evaluate(model, X_test, y_test):
    logger.info(f"Evaluating model performance. Score={model.score(X_test, y_test)}")
    return model.score(X_test, y_test)

def save_model(model):
    logger.info(f"saving the model to a directory {model_settings.model_path}/{model_settings.model_name}")
    pk.dump(model, open(f'{model_settings.model_path}/{model_settings.model_name}', 'wb')) # model_path + model_name