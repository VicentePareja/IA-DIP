# entrenar_modelo.py
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from parametros import (ANCHO_MAPA_ENTRENAR, LARGO_MAPA_ENTRENAR, PATH_ALMACENAR_MODELO,
                        PATH_CARGAR_DATOS)
from recursos.funciones_auxiliares import printear_mapa, printear_un_ejemplo
from joblib import dump, load
import numpy as np
import pandas as pd
import logging
import time

logging.basicConfig(level=logging.INFO)

def load_data():
    logging.info("Cargando datos desde el archivo CSV...")
    start_time = time.time()
    
    try:
        dataframe = pd.read_csv(PATH_CARGAR_DATOS)
    except FileNotFoundError:
        logging.error("No se pudo abrir el archivo CSV.")
        return None

    logging.info("Datos cargados con éxito en {:.2f} segundos.".format(time.time() - start_time))
    output_columns = ['tablero_final_' + str(i) for i in range(ANCHO_MAPA_ENTRENAR*LARGO_MAPA_ENTRENAR)]
    X = dataframe.drop(output_columns, axis=1).values
    Y = dataframe[output_columns].values
    return train_test_split(X, Y, test_size=0.2, random_state=42)

def train_model(X_train, Y_train):
    logging.info("Entrenando el modelo...")
    start_time = time.time()
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    model = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=50000, random_state=42)
    model.fit(X_train, Y_train)

    logging.info("Modelo entrenado con éxito en {:.2f} segundos.".format(time.time() - start_time))
    dump(model, PATH_ALMACENAR_MODELO)
    return model, scaler

def evaluate_model(model, scaler, X_train, X_test, Y_test):
    logging.info("Evaluando el modelo...")
    start_time = time.time()

    X_test = scaler.transform(X_test)
    Y_pred = model.predict(X_test)
    for i in range(2):
        printear_un_ejemplo(X_train, Y_test, Y_pred, (ANCHO_MAPA_ENTRENAR, LARGO_MAPA_ENTRENAR), index=i)

    mse = mean_squared_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)

    logging.info("Evaluación completada en {:.2f} segundos.".format(time.time() - start_time))
    logging.info(f"MSE: {mse}, RMSE: {rmse}, MAE: {mae}, R^2: {r2}")

if __name__ == "__main__":
    X_train, X_test, Y_train, Y_test = load_data()
    model, scaler = train_model(X_train, Y_train)
    evaluate_model(model, scaler, X_train, X_test, Y_test)



