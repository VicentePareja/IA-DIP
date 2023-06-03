from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# Generar datos de ejemplo
# Leer el archivo CSV
dataframe = pd.read_csv('simulacion.csv')

# Crear la lista de nombres de las columnas de salida
output_columns = ['tablero_final_' + str(i+1) for i in range(10)]

# Separar las columnas de entrada y salida
X = dataframe.drop(output_columns, axis=1).values
Y = dataframe[output_columns].values


# Dividir los datos en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear el modelo
model = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=50000, random_state=42)

# Entrenar el modelo
model.fit(X_train, Y_train)

# Predecir los valores de prueba
Y_pred = model.predict(X_test)

print(Y_pred)

