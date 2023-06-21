# fucionar_imagenes.py - Fusiona dos imágenes en una sola imagen

from PIL import Image
from parametros import (ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR, PATH_IMAGENES_FUSIONADAS,
                        PATH_ALMACENAR_RESULTADOS, PATH_CARGAR_IMAGENES)

# Abre las dos imágenes

img1 = Image.open(PATH_ALMACENAR_RESULTADOS + '/imagen_prediccion_12.jpg')
img2 = Image.open(PATH_CARGAR_IMAGENES + '/sin incendio/Incendio 1.jpeg')

# Redimensiona la segunda imagen al tamaño de la primera imagen
img1 = img1.resize(img2.size)

# Convierte las imágenes a formato RGBA para poder trabajar con los canales de color
img1 = img1.convert("RGBA")
img2 = img2.convert("RGBA")

# Crea una nueva imagen en blanco del mismo tamaño que las imágenes de entrada
final = Image.new("RGBA", img1.size)

# Itera sobre cada píxel de las imágenes
for x in range(img1.width):
    for y in range(img1.height):
        r1, g1, b1, a1 = img1.getpixel((x, y))
        r2, g2, b2, a2 = img2.getpixel((x, y))
        
        # Verifica si el color de la primera imagen es intenso
        if (r1 > 50 and g1 > 50 and b1 > 50):
            final.putpixel((x, y), (r1, g1, b1, a1))
        else:
            final.putpixel((x, y), (r2, g2, b2, a2))

# Guarda la imagen final
final.convert("RGB").save(PATH_IMAGENES_FUSIONADAS + "/imagen_fusionada.jpg")

