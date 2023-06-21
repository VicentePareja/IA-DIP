# parametros.py

# Generar datos
N_SIMULACIONES = 5
ANCHO_MAPA_CREAR = 90
LARGO_MAPA_CREAR = 90
PROB_RADIACION = 12
PROB_VIENTO = 5

FOCOS_ALEATORIOS = False

# Entrenar un modelo
TIEMPO_SIMULACION = 15
ANCHO_MAPA_ENTRENAR = 90
LARGO_MAPA_ENTRENAR = 90
N_NEURONAS = 100
PRINT_EJEMPLOS = False


# Predecir con un modelo

ANCHO_MAPA_MODELO = 90
LARGO_MAPA_MODELO = 90

# paths
PATH_CARGAR_DATOS = 'imagenes/nuevas imágenes/imágenes.csv'
PATH_CARGAR_MODELO = 'modelos_entrenados/modelo_entrenado102.joblib'
PATH_ALMACENAR_MODELO = 'modelos_entrenados/modelo_entrenado102.joblib'
PATH_ALMACENAR_DATOS = 'simulaciones/simulaciones_homogéneas/simulacion_homogenea7.csv'

# visualización
ALPHA = 500
IMAGENES = True
SIZE_IMAGENES = (300, 300)

# Procesar Imagenes

PATH_IMAGENES_CSV = 'imagenes/nuevas imágenes/imágenes.csv'
PATH_CARGAR_IMAGENES = 'imagenes/imágenes satelitales'
PATH_ALMACENAR_RESULTADOS = 'imagenes/Resultados predicciones'
PATH_IMAGENES_FUSIONADAS = 'imagenes/Resultados fusionados'
