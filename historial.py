# historial.py
import numpy as np


class Historial:
    def __init__(self):
        self.historial = []

    def agregar(self, mapa):
        aux = np.zeros_like(mapa.mapa, dtype=int)  # Inicializamos con ceros usando NumPy.
        for i in range(mapa.largo):
            for j in range(mapa.ancho):
                if mapa.mapa[i, j].estado:
                    aux[i, j] = 1000
                else:
                    aux[i, j] = int(mapa.mapa[i, j].prob*100)
        self.historial.append(aux)