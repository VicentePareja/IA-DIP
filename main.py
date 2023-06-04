# main.py
from simulacion import simular
from mapa import Mapa
from historial import Historial
from parametros import N_SIMULACIONES, ANCHO_MAPA, LARGO_MAPA, TIEMPO_SIMULACION
import pandas as pd

if "__main__" == __name__:

    filas = []
    for _ in range(N_SIMULACIONES):  # simular n veces
       
        if _ % (N_SIMULACIONES//1) == 0:
            print("Simulación número", _)

        tablero = Mapa(ANCHO_MAPA, LARGO_MAPA)
        historial = Historial()

        filas_simulacion = simular(tablero, historial, TIEMPO_SIMULACION)
        filas.extend(filas_simulacion)  # Agrega todas las filas de esta simulación a la lista principal de filas

    df = pd.DataFrame(filas)
    df.to_csv("simulaciones/simulacion13.csv", index=False)


