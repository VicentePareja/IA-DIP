# fucionar_imagenes.py - Fusiona dos imágenes en una sola imagen

from PIL import Image
from parametros import (ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR, PATH_IMAGENES_FUSIONADAS,
                        PATH_ALMACENAR_RESULTADOS, PATH_CARGAR_IMAGENES)
from recursos.visualizacion import almacenar_ejemplo_imagen, fusionar_imagenes

# Abre las dos imágenes

img1 = Image.open(PATH_ALMACENAR_RESULTADOS + '/imagen_prediccion_12.jpg')
img2 = Image.open(PATH_CARGAR_IMAGENES + '/sin incendio/Incendio 1.jpeg')
