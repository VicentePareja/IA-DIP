# funciones_auxiliares.py
from parametros import ALPHA, PATH_ALMACENAR_RESULTADOS
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


def mostrar_imagen(imagen, titulo, ancho, largo):
    """
    Muestra una imagen a partir de una matriz numpy 1D.

    Parámetros:
    imagen -- matriz numpy 1D
    titulo -- título de la imagen
    ancho -- ancho de la imagen original
    largo -- largo de la imagen original
    """
    # Redimensiona la matriz 1D a una matriz 2D
    imagen = imagen.reshape((ancho, largo))

    # Muestra la imagen
    plt.figure()  # Crea una nueva figura
    plt.imshow(imagen, cmap='hot')
    plt.title(titulo)
    plt.colorbar()
    plt.show(block=False)  # Muestra la imagen sin bloquear el resto del código


def printear_un_ejemplo_imagen(X_train, Y_test, Y_pred, shape, index=0):
    print("Ejemplo", index)

    # Crea una figura y un conjunto de subtramas
    fig, axs = plt.subplots(1, 3)

    tiempo = X_train[index][0]
    print(f"Tiempo: {tiempo}")

    # Redimensiona la matriz 1D a una matriz 2D
    inicial = X_train[index][1:].reshape(*shape)
    real = Y_test[index].reshape(*shape)
    pred = Y_pred[index].reshape(*shape)

    # Muestra las imágenes
    axs[0].imshow(inicial, cmap='hot')
    axs[0].set_title("Inicial")
    axs[1].imshow(real, cmap='hot')
    axs[1].set_title("Real")
    axs[2].imshow(pred, cmap='hot')
    axs[2].set_title("Predicción")

    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    # Guarda la figura antes de mostrarla
    plt.savefig(PATH_ALMACENAR_RESULTADOS + f'/imagen_ejemplo_{index}.jpg')

    # Muestra la figura con todas las imágenes
    plt.show()


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
