# Predictor.py
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd

# Leer el archivo CSV
dataframe = pd.read_csv('simulaciones/simulacion13.csv')

# Crear la lista de nombres de las columnas de salida
output_columns = ['tablero_final_' + str(i) for i in range(15*15)]

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

# Predecir los valores de prueba
Y_pred = model.predict(X_test)

# Selecciona un caso de prueba particular (por ejemplo, el primer caso)
index = 0
print("Características de entrada:", X_test[index])
print("Valor real:", Y_test[index])
print("Valor predicho:", Y_pred[index])

# Calcular métricas de rendimiento
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R^2:", r2)


