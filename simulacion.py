# simulacion.py
import random
import numpy as np
import pandas as pd
from mapa import Mapa
from historial import Historial

def simular(tablero, historial, tiempo):
    foco_inicial_x = random.randint(0, tablero.ancho-1)
    foco_inicial_y = random.randint(0, tablero.largo-1)
    tablero.mapa[foco_inicial_y][foco_inicial_x].cambiar_estado(True)
    viento = [random.randint(0,3)] + random.sample([-1, -1, -1, -1, 0, 1, 1, 1, 1], 2)
    tablero.viento = viento
    tablero.actualizar()
    historial.agregar(tablero)

    filas = []  # Inicia una lista vacía para almacenar las filas

    for t in range(1, tiempo):
        tablero.quemar()
        tablero.actualizar()
        historial.agregar(tablero)

        # transformar la entrada y salida a un formato "aplanado"
        foco_inicial = [foco_inicial_x, foco_inicial_y]
        tablero_inicial = [val for sublist in historial.historial[0] for val in sublist]
        tablero_final = [val for sublist in historial.historial[-1] for val in sublist]
        viento = tablero.viento
        tiempo = t

        # agregar a un diccionario que representa una fila
        fila = {"foco_inicial_x": foco_inicial[0], "foco_inicial_y": foco_inicial[1],
                "tamaño_viento": viento[0], "viento_x": viento[1], "viento_y": viento[2],
                "tiempo": tiempo}
        for i in range(len(tablero_inicial)):
            fila["tablero_inicial_"+str(i)] = tablero_inicial[i]
            fila["tablero_final_"+str(i)] = tablero_final[i]
        
        filas.append(fila)  # Agrega la fila a la lista de filas

    return filas

if __name__ == "__main__":
    # Crear una instancia de Mapa y Historial
    tablero = Mapa(5, 5)
    historial = Historial()

    # Realizar la simulación
    resultado = simular(tablero, historial, 20)

    # Imprimir el resultado de cada fila
    for i, fila in enumerate(resultado):
        print(f"--- Resultado de la simulación {i+1} ---")
        print(f"Foco inicial: ({fila['foco_inicial_x']}, {fila['foco_inicial_y']})")
        print(f"Tamaño del viento: {fila['tamaño_viento']}")
        print(f"Dirección del viento: ({fila['viento_x']}, {fila['viento_y']})")
        print(f"Tiempo: {fila['tiempo']}")

        # Imprimir el tablero para cada tiempo
        for j in range(tablero.ancho * tablero.largo):
            print(f"Tiempo {i+1}:")
            print(np.array([fila['tablero_inicial_'+str(i)] for i in range(tablero.ancho * tablero.largo)]).reshape(tablero.ancho, tablero.largo))
        print("\n")