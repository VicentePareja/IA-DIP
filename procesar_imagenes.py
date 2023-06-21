# procesar_imagenes.py

from PIL import Image
from parametros import ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR, PATH_IMAGENES_CSV, PATH_CARGAR_IMAGENES
import numpy as np
import os
import csv


def get_red_pixels(img, threshold=100):
    # Crea una nueva matriz del mismo tamaño que la imagen original pero llena de ceros
    new_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

    # Recorre cada pixel de la imagen
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Si el pixel es "rojo" según el umbral definido, cambia el valor correspondiente
            # en la nueva matriz a 1
            if img[i, j, 0] - max(img[i, j, 1], img[i, j, 2]) > threshold:
                new_img[i, j] = 1  # rojo se convierte en 1
            else:
                new_img[i, j] = 0  # no rojo se convierte en 0
    return new_img


def process_folder(folder_path, id_incendio, standard_size=(ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR), threshold=100):
    # Abre la imagen inicial
    im_inicial = Image.open(folder_path + '/Imagen 001.jpeg')
    print(len(im_inicial.getdata()))

    # Redimensiona la imagen al tamaño estándar
    im_inicial = im_inicial.resize(standard_size, Image.ANTIALIAS)

    # Convierte la imagen a una matriz numpy para facilitar el procesamiento
    np_im_inicial = np.array(im_inicial, dtype=np.int16)

    # Obtiene los píxeles rojos
    new_np_im_inicial = get_red_pixels(np_im_inicial, threshold)

    # Aplana la matriz 2D en una matriz 1D
    flattened_np_im_inicial = new_np_im_inicial.flatten()

    # Recorre cada archivo en la carpeta
    for index, filename in enumerate(os.listdir(folder_path), start=1):
        # Asegúrate de que el archivo es una imagen .jpeg
        if filename.endswith('.jpeg'):
            # Abre la imagen
            im = Image.open(os.path.join(folder_path, filename))

            # Redimensiona la imagen al tamaño estándar
            im = im.resize(standard_size, Image.ANTIALIAS)

            # Convierte la imagen a una matriz numpy para facilitar el procesamiento
            np_im = np.array(im, dtype=np.int16)

            # Obtiene los píxeles rojos
            new_np_im = get_red_pixels(np_im, threshold)

            # Aplana la matriz 2D en una matriz 1D
            flattened_np_im = new_np_im.flatten()

            # Escribe los datos en el archivo .csv
            with open(PATH_IMAGENES_CSV, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([id_incendio] + [index] + list(flattened_np_im_inicial) + list(flattened_np_im))

            # Actualiza la imagen inicial para la próxima iteración
            np_im_inicial = np_im
            new_np_im_inicial = new_np_im
            flattened_np_im_inicial = flattened_np_im


def create_columns():
    # Define los nombres de las columnas
    standard_size = (ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR)  # Ajusta esto al tamaño que prefieras
    columns = ['id_incendio'] + ['tiempo'] + \
        [f'tablero_inicial_{i - 1}' for i in range(1, standard_size[0]*standard_size[1] + 1)] \
        + [f'tablero_final_{i - 1}' for i in range(1, standard_size[0]*standard_size[1] + 1)]

    # Crea un archivo .csv y escribe los nombres de las columnas
    with open(PATH_IMAGENES_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)


def create_data(carpeta_inicial=1, carpeta_final=None):

    if carpeta_final is None:
        carpeta_final = carpeta_inicial

    # Recorre cada carpeta
    for i in range(carpeta_inicial, carpeta_final + 1):
        folder_path = PATH_CARGAR_IMAGENES + '/incendio ' + str(i)
        process_folder(folder_path, i)


if '__main__' == __name__:

    # Crea las columnas del archivo .csv
    create_columns()

    # Crea los datos
    create_data(1, 5)
