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

    def imprimir(self):
        for i in range(len(self.historial)):
            matriz = np.array(self.historial[i])

            np.savetxt("matriz_bonita.txt", matriz, fmt="%4d")
            with open("matriz_bonita.txt", "r") as file:
                print(file.read())