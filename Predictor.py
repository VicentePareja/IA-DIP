# Predictor.py
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from parametros import ANCHO_MAPA_ENTRENAR, LARGO_MAPA_ENTRENAR
import numpy as np
import pandas as pd

tx, ty = ANCHO_MAPA_ENTRENAR, LARGO_MAPA_ENTRENAR



def printear_mapa(mapa, n, m, alpha=500):
    for i in range(n):
        for j in range(m):
            if mapa[i, j] - 1000 >= -alpha:
                print("🔥", end=" ")
            elif mapa[i, j] < alpha:
                print("🌲", end=" ")
            else:
                print(int(mapa[i, j]), end=" ")
        print()
    print("\n")


def printear_un_ejemplo(index=0):

    print("Condiciones iniciales:")
    print(f"Viento: {X_test_original[index][2:5]}, Tiempo transcurrido: {X_test_original[index][5]}\n")
    print("Mapa Inicial:\n")
    printear_mapa(X_test_original[index][6:].reshape(tx, ty), tx, ty)
    print("Mapa Final:\n")
    printear_mapa(Y_test[index].reshape(tx, ty), tx, ty)
    print("Mapa Predicho:\n")
    printear_mapa(Y_pred[index].reshape(tx, ty), tx, ty)


# Leer el archivo CSV
dataframe = pd.read_csv('simulaciones/simulacion_arbitraria.csv')

# Crear la lista de nombres de las columnas de salida
output_columns = ['tablero_final_' + str(i) for i in range(tx*ty)]

# Separar las columnas de entrada y salida
X = dataframe.drop(output_columns, axis=1).values
Y = dataframe[output_columns].values

# Dividir los datos en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test_original = X_test
X_test = scaler.transform(X_test)

# Crear el modelo
model = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=50000, random_state=42)

# Entrenar el modelo
model.fit(X_train, Y_train)

# Predecir los valores de prueba
Y_pred = model.predict(X_test)

# Printear 10 casos para ver cómo se comporta el modelo
for i in range(10):
    printear_un_ejemplo(i)

# Calcular métricas de rendimiento
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R^2:", r2)


