# Predictor_Incendios.py

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from parametros import ANCHO_MAPA_MODELO, LARGO_MAPA_MODELO
from funciones_auxiliares import printear_mapa, printear_un_ejemplo
from joblib import dump, load
import numpy as np
import pandas as pd

tx, ty = ANCHO_MAPA_MODELO, LARGO_MAPA_MODELO

path_modelo = 'modelos_entrenados/modelo_entrenado1.joblib'
path_datos = 'simulaciones/simulacion_arbitraria.csv'

# Cargar el modelo
model = load(path_modelo)

# Leer el archivo CSV
dataframe = pd.read_csv(path_datos)

# Crear la lista de nombres de las columnas de salida
output_columns = ['tablero_final_' + str(i) for i in range(tx*ty)]

# Separar las columnas de entrada y salida
X = dataframe.drop(output_columns, axis=1).values
Y = dataframe[output_columns].values

# Evaluar el modelo en un ejemplo
Y_pred = model.predict(X[:2])

print(len(X[:2]), len(Y[:2]), len(Y_pred[:2]))  

for i in range(2):
    # Imprimir un ejemplo
    printear_un_ejemplo(X[:2], Y[:2], Y_pred[:2], (tx, ty), index=i)
