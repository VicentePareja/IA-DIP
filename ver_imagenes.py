# ver_imagenes.py

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from parametros import (ANCHO_MAPA_MODELO, LARGO_MAPA_MODELO, PATH_CARGAR_DATOS, PATH_CARGAR_MODELO,
                        IMAGENES)
from recursos.funciones_auxiliares import (printear_mapa, printear_un_ejemplo, 
                                           printear_un_ejemplo_imagen)
from joblib import dump, load
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tx, ty = ANCHO_MAPA_MODELO, LARGO_MAPA_MODELO

# Leer el archivo CSV para predecir resultados
dataframe = pd.read_csv(PATH_CARGAR_DATOS)

# Crear la lista de nombres de las columnas de salida
output_columns = ['tablero_final_' + str(i) for i in range(tx*ty)]

# Separar las columnas de entrada y salida
X = dataframe.drop(output_columns, axis=1).values
Y = dataframe[output_columns].values

# Recorre cada ejemplo en X y Y
for i in range(5):
    index = randint(0, len(X) - 1)
    print(f'Ejemplo: {index}')
    printear_un_ejemplo_imagen(X, Y, Y, (tx, ty), index = i)