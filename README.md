# IA-DIP: Simulación y Predicción de Incendios Forestales

IA-DIP es un proyecto que simula incendios forestales y utiliza una Red Neuronal Artificial (RNA) para predecir la propagación del fuego. El proyecto consta de dos módulos principales: la simulación y la predicción.

## Módulo de Simulación

La simulación se implementa en Python, con ayuda de las bibliotecas NumPy y Pandas.

La simulación representa un bosque como una cuadrícula 2D. Cada celda en esta cuadrícula representa un parche de bosque que puede estar en llamas o no. La propagación del fuego se ve influenciada por la dirección e intensidad del viento, y la probabilidad de que una celda se incendie depende de los estados de sus celdas vecinas.

## Módulo de Predicción

El módulo de predicción emplea un Regresor de Perceptrón Multicapa (MLP) de la biblioteca sklearn. El modelo predice el estado final del bosque dado las condiciones iniciales y los datos del viento, y se entrena con datos generados por el simulador.

## Comenzando

### Dependencias

Este proyecto requiere Python 3.8 o una versión más reciente. Además, depende de las siguientes bibliotecas de Python:

- NumPy
- Pandas
- sklearn
- joblib

Estas bibliotecas se pueden instalar usando pip:

\```shell
pip install numpy pandas sklearn joblib
\```

## Instalación

Clone el proyecto en su máquina local:

\```shell
git clone https://github.com/yourusername/IA-DIP.git
\```

## Uso

Para usar este proyecto, primero ejecute la simulación para generar datos:

\```shell
python crear_datos.py
\```

Esto simulará un incendio forestal y guardará los estados iniciales y finales del bosque en un archivo CSV.

Para entrenar y probar el modelo de predicción utilizando los datos generados, use el siguiente comando:

\```shell
python entrenar_modelo.py
\```

Esto entrenará un Regresor MLP utilizando los datos generados y guardará el modelo entrenado.

Finalmente, para realizar predicciones utilizando el modelo entrenado, use:

\```shell
python predictor_incendios.py
\```

## Contribuyendo

Las contribuciones, problemas y solicitudes de funciones son bienvenidas. Para cambios importantes, por favor abra un problema primero para discutir lo que le gustaría cambiar.

## Licencia

Tenga en cuenta que este proyecto está licenciado bajo la licencia MIT, y todo el código contribuido también estará licenciado bajo MIT. Para obtener más información, consulte el archivo LICENSE.
