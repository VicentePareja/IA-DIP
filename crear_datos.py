# main.py
from simulacion import simular, simular_foco
from mapa import Mapa
from historial import Historial
from parametros import N_SIMULACIONES, ANCHO_MAPA_SIMULAR, LARGO_MAPA_SIMULAR, TIEMPO_SIMULACION
import pandas as pd
import time 

focos_aleatorios = False
path = "simulaciones/simulacion_arbitraria.csv"

if "__main__" == __name__:
    
    filas = []
    inicio = time.time()
    foco_actual_x = 0
    foco_actual_y = 0
    for _ in range(N_SIMULACIONES):  # simular n veces
       
        try:
            if _ % (N_SIMULACIONES//10) == 0:
                print("Simulación número", _)
        except ZeroDivisionError:
            pass

        tablero = Mapa(ANCHO_MAPA_SIMULAR, LARGO_MAPA_SIMULAR)
        historial = Historial()

        if focos_aleatorios:

            filas_simulacion = simular(tablero, historial, TIEMPO_SIMULACION)
            filas.extend(filas_simulacion)  # Agrega todas las filas de esta simulación a la lista principal de filas

        else: # Datos homogéneos

            foco_actual_x = (foco_actual_x + 1) % ANCHO_MAPA_SIMULAR
            if foco_actual_x == 0:
                foco_actual_y = (foco_actual_y + 1) % LARGO_MAPA_SIMULAR

            filas_simulacion = simular_foco(tablero, historial, TIEMPO_SIMULACION, foco_actual_x, foco_actual_y)
            filas.extend(filas_simulacion)

    fin_simulaciones = time.time()
    print("Tiempo de simulación:", fin_simulaciones - inicio)
    df = pd.DataFrame(filas)
    print("dataframe creado")
    df.to_csv(path, index=False)
    fin = time.time()

    print(f"Simulaciones guardadas en: {path}")    
    print("Tiempo de simulación:", fin_simulaciones - inicio)
    print("Tiempo total:", fin - inicio)


