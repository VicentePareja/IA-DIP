# crear_datos.py
from recursos.simulacion import simular, simular_foco
from recursos.mapa import Mapa
from recursos.historial import Historial
from parametros import (N_SIMULACIONES, ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR, TIEMPO_SIMULACION,
                        PATH_ALMACENAR_DATOS, FOCOS_ALEATORIOS)
import pandas as pd
import time
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)


def ejecutar_simulacion():
    """
    Ejecuta N_SIMULACIONES simulaciones y recoge los resultados en una lista de filas.
    Devuelve la lista de filas recogida.
    """
    filas = []
    foco_actual_x = 0
    foco_actual_y = 0

    # Ejecuta N_SIMULACIONES simulaciones
    for simulacion_num in tqdm(range(N_SIMULACIONES), desc="Progreso de la simulación"):
        try:
            
            tablero = Mapa(ANCHO_MAPA_CREAR, LARGO_MAPA_CREAR)
            historial = Historial()

            # Decide si la simulación es aleatoria o homogénea basándose en FOCOS_ALEATORIOS
            if FOCOS_ALEATORIOS:
                filas.extend(simular(tablero, historial, TIEMPO_SIMULACION))
            else:  # Datos homogéneos
                foco_actual_x = (foco_actual_x + 1) % ANCHO_MAPA_CREAR
                if foco_actual_x == 0:
                    foco_actual_y = (foco_actual_y + 1) % LARGO_MAPA_CREAR

                filas.extend(simular_foco(tablero, historial, TIEMPO_SIMULACION, foco_actual_x, foco_actual_y))
        except Exception as e:
            logging.error(f"Error durante la simulación número {simulacion_num}: {e}")

    return filas


if __name__ == "__main__": 
    inicio = time.time()

    try:
        filas = ejecutar_simulacion()
        fin_simulacion = time.time()

        logging.info("Creando dataframe...")
        df = pd.DataFrame(filas)
        logging.info("Dataframe creado\n")

        df.to_csv(PATH_ALMACENAR_DATOS, index=False)
        fin_almenamiento = time.time()
        logging.info(f"Simulaciones guardadas en: {PATH_ALMACENAR_DATOS}\n")


        fin = time.time()
        logging.info(f"Tiempo de simulación: {fin_simulacion - inicio:.2f} segundos")
        logging.info(f"Tiempo de almacenamiento: {fin_almenamiento - fin_simulacion:.2f} segundos")
        logging.info(f"Tiempo total: {fin - inicio:.2f} segundos")

    except Exception as e:
        logging.error(f"Error durante el procesamiento de los datos: {e}")

