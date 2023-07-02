# IA-DIP: Simulación y Predicción de Incendios Forestales con Inteligencia Artificial

IA-DIP es un proyecto de simulación y predicción de incendios forestales basado en técnicas de aprendizaje automático. El proyecto consta de dos módulos principales: el Módulo de Simulación y el Módulo de Predicción. 

## Módulo de Simulación

El módulo de simulación, implementado en Python, emplea las bibliotecas NumPy y Pandas para crear una representación en cuadrícula 2D de un bosque. Cada celda de esta cuadrícula representa un parche de bosque, que puede estar en llamas o no. La dirección e intensidad del viento influyen en la propagación del fuego, y la probabilidad de que un parche de bosque se incendie depende de los estados de sus parches vecinos.

## Módulo de Predicción

El módulo de predicción utiliza un Regresor de Perceptrón Multicapa (MLP) de la biblioteca sklearn para predecir el estado final del bosque dadas las condiciones iniciales y los datos del viento. El modelo se entrena con datos generados por el simulador. También se incluye una funcionalidad para visualizar las predicciones del modelo en forma de imágenes, facilitando la interpretación de los resultados de la predicción.

## Comenzando

### Dependencias

Este proyecto requiere Python 3.8 o una versión más reciente. También necesitarás las siguientes bibliotecas de Python:

- NumPy
- Pandas
- sklearn
- joblib
- matplotlib
- Pillow

Puedes instalar estas bibliotecas usando pip:

\```shell
pip install numpy pandas sklearn joblib matplotlib pillow
\```

### Instalación

Para instalar el proyecto, clónalo en tu máquina local:

```shell
git clone https://github.com/VicentePareja/IA-DIP.git
```

## Uso

Primero, ejecuta la simulación para generar datos:

```shell
python crear_datos.py
```

Esto simulará un incendio forestal y guardará los estados iniciales y finales del bosque en un archivo CSV.

Después, entrena y prueba el modelo de predicción utilizando los datos generados:

```shell
python entrenar_modelo.py
```

Esto entrenará un Regresor MLP utilizando los datos generados y guardará el modelo entrenado para futuras predicciones.

Finalmente, realiza predicciones utilizando el modelo entrenado:

```shell
python predictor_incendios.py
```

## Contribuyendo

Las contribuciones, problemas y solicitudes de características son bienvenidos. Para cambios importantes, por favor abre un problema primero para discutir lo que te gustaría cambiar.

## Licencia

Este proyecto está licenciado bajo la licencia PUC. Por favor, ten en cuenta que cualquier contribución que realices también estará sujeta a esta licencia. Para más detalles, consulta el archivo LICENSE en el repositorio.
