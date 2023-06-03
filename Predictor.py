from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Generar datos de ejemplo
X = np.random.rand(100, 5)  # 100 ejemplos, cada uno con 5 características
Y = np.random.rand(100, 3)  # 100 ejemplos de salidas, cada una con 3 valores

# Dividir los datos en entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear el modelo
model = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=500, random_state=42)

# Entrenar el modelo
model.fit(X_train, Y_train)

# Predecir los valores de prueba
Y_pred = model.predict(X_test)

print(Y_pred)

