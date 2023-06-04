# main.py
from simulacion import simular
from mapa import Mapa
from historial import Historial
import parametros as p
import pandas as pd

if "__main__" == __name__:

    filas = []
    for _ in range(p.N_SIMULACIONES):  # simular 100 veces
        tablero = Mapa(p.ANCHO_MAPA, p.LARGO_MAPA)
        historial = Historial()

        filas_simulacion = simular(tablero, historial, p.TIEMPO_SIMULACION)
        filas.extend(filas_simulacion)  # Agrega todas las filas de esta simulación a la lista principal de filas

    df = pd.DataFrame(filas)
    df.to_csv("simulaciones/simulacion10.csv", index=False)


