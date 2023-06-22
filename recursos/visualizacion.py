# visualizacion.py
from parametros import (ALPHA, PATH_ALMACENAR_RESULTADOS, PATH_IMAGENES_FUSIONADAS,
                        PATH_ALMACENAR_RESULTADOS, PATH_CARGAR_IMAGENES)
from PIL import Image
import matplotlib.pyplot as plt
import threading


def printear_mapa(mapa, n, m, alpha=ALPHA):

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


def printear_un_ejemplo(X_test, Y_test, Y_pred, tamaño, index=0):

    tx, ty = tamaño
    print("Condiciones iniciales:")
    print(f"Viento: {X_test[index][2:5]} Tiempo transcurrido: {X_test[index][5]}")
    print("\n")
    print("Mapa Inicial:\n")
    printear_mapa(X_test[index][6:].reshape(tx, ty), tx, ty)
    print("Mapa Final:\n")
    printear_mapa(Y_test[index].reshape(tx, ty), tx, ty)
    print("Mapa Predicho:\n")
    printear_mapa(Y_pred[index].reshape(tx, ty), tx, ty)


def fusionar_imagenes(imagen1, imagen2, index, imagen_tipo="prediccion"):
    # Abre las dos imágenes
    img1 = Image.open(PATH_ALMACENAR_RESULTADOS + imagen1)
    img2 = Image.open(PATH_CARGAR_IMAGENES + imagen2)

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
    path_imagen_fusionada = PATH_IMAGENES_FUSIONADAS + f"/imagen_fusionada_{imagen_tipo}_{index}.jpg"
    final.convert("RGB").save(path_imagen_fusionada)

    return path_imagen_fusionada


def guardar_subimagen(fig, ax, titulo, index):
    """
    Guarda una subimagen específica de una figura.

    Parámetros:
    fig -- la figura que contiene el subgráfico
    ax -- el subgráfico a guardar
    titulo -- título de la subimagen
    index -- índice del ejemplo
    """
    # Crea los bordes de la subimagen
    extent = ax.get_tightbbox(fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())

    # Guarda la subimagen
    fig.savefig(PATH_ALMACENAR_RESULTADOS + f'/imagen_{titulo}_{index}.jpg',
                bbox_inches=extent)


def printear_un_ejemplo_imagen(X_train, Y_test, Y_pred, shape, index=0):

    print("Ejemplo", index)
    id_incendio = X_train[index][0]
    tiempo = X_train[index][1]
    print(f"Tiempo: {tiempo}")

    # Redimensiona la matriz 1D a una matriz 2D
    inicial = X_train[index][2:].reshape(*shape)
    real = Y_test[index].reshape(*shape)
    pred = Y_pred[index].reshape(*shape)

    # Crea una figura y un conjunto de subtramas
    fig, axs = plt.subplots(1, 3)

    # Muestra las imágenes
    axs[0].imshow(inicial, cmap='hot')
    axs[1].imshow(real, cmap='hot')
    axs[2].imshow(pred, cmap='hot')

    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')  # No muestra el marco de los subplots

    # Guarda cada subimagen
    guardar_subimagen(fig, axs[0], "inicial", index)
    guardar_subimagen(fig, axs[1], "real", index)
    guardar_subimagen(fig, axs[2], "prediccion", index)

    # Fusiona y guarda la imagen inicial y predicción
    imagen_fusionada_path = fusionar_imagenes(f'/imagen_prediccion_{index}.jpg',
                                              f'/sin incendio/Incendio {id_incendio}.jpeg',
                                              index, "prediccion")

    print(f"Imagen fusionada guardada en: {imagen_fusionada_path}")

    # Fusiona y guarda la imagen inicial y real
    imagen_fusionada_real_path = fusionar_imagenes(f'/imagen_real_{index}.jpg',
                                                   f'/sin incendio/Incendio {id_incendio}.jpeg',
                                                   index, "real")

    print(f"Imagen fusionada real guardada en: {imagen_fusionada_real_path}")


if __name__ == "__main__":

    import logging
    import time
    import pandas as pd
    from parametros import (ANCHO_MAPA_ENTRENAR, LARGO_MAPA_ENTRENAR, PATH_CARGAR_DATOS)

    logging.info("Cargando datos desde el archivo CSV...")
    start_time = time.time()

    try:
        dataframe = pd.read_csv(PATH_CARGAR_DATOS)
        logging.info("Datos cargados con éxito en {:.2f} segundos.".format(time.time() - start_time))
        output_columns = ['tablero_final_' + str(i) for i in range(ANCHO_MAPA_ENTRENAR*LARGO_MAPA_ENTRENAR)]
        X = dataframe.drop(output_columns, axis=1).values
        Y = dataframe[output_columns].values
        # Print an example
        index = 0  # Change this to the index of the example you want to print
        printear_un_ejemplo_imagen(X, Y, Y, (ANCHO_MAPA_ENTRENAR, LARGO_MAPA_ENTRENAR))

    except FileNotFoundError:
        logging.error("No se pudo abrir el archivo CSV.")
