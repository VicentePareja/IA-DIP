# main.py
from simulacion import simular
from mapa import Mapa
from historial import Historial
from parametros import N_SIMULACIONES, ANCHO_MAPA, LARGO_MAPA, TIEMPO_SIMULACION
import pandas as pd
import time 

if "__main__" == __name__:
    path = "simulaciones/simulacion_arbitraria.csv"

    filas = []
    inicio = time.time()
    for _ in range(N_SIMULACIONES):  # simular n veces
       
        try:
            if _ % (N_SIMULACIONES//10) == 0:
                print("Simulación número", _)
        except ZeroDivisionError:
            pass

        tablero = Mapa(ANCHO_MAPA, LARGO_MAPA)
        historial = Historial()

        filas_simulacion = simular(tablero, historial, TIEMPO_SIMULACION)
        filas.extend(filas_simulacion)  # Agrega todas las filas de esta simulación a la lista principal de filas
    fin_simulaciones = time.time()
    print("Tiempo de simulación:", fin_simulaciones - inicio)
    df = pd.DataFrame(filas)
    print("dataframe creado")
    df.to_csv(path, index=False)
    fin = time.time()

    print(f"Simulaciones guardadas en: {path}")    
    print("Tiempo de simulación:", fin_simulaciones - inicio)
    print("Tiempo total:", fin - inicio)


