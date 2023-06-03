import numpy as np
import pandas as pd
import random
import parametros as p

class Mapa:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        self.mapa = np.full((largo, ancho), Casilla())  # Aquí usamos NumPy para inicializar la matriz.
        self.viento = [0,0,0]

    def actualizar(self):
        for i in range(self.largo):
            for j in range(self.ancho):
                if self.mapa[i, j].estado:
                    prob = random.randint(0,25)/100

                    # Verificar índices antes de acceder
                    if i < self.largo - 1:
                        self.mapa[i + 1, j].cambiar_prob(prob)
                    if i > 0:
                        self.mapa[i - 1, j].cambiar_prob(prob)
                    if j < self.ancho - 1:
                        self.mapa[i, j + 1].cambiar_prob(prob)
                    if j > 0:
                        self.mapa[i, j - 1].cambiar_prob(prob)

                    for _ in range(1, self.viento[0] + 1):
                        if j + self.viento[2]*_ < self.ancho:
                            self.mapa[i, j + self.viento[2]*_].cambiar_prob((self.viento[0] + 1 -_)*prob)
                        if i + self.viento[1]*_ < self.largo:
                            self.mapa[i + self.viento[1]*_, j].cambiar_prob((self.viento[0] + 1 -_)*prob)

    def quemar(self):
        for i in range(self.largo):
            for j in range(self.ancho):
                if random.random() <= self.mapa[i, j].prob:
                    self.mapa[i, j].cambiar_estado(True)
                self.mapa[i, j].reiniciar_prob()         

class Casilla:
    def __init__(self):
        self.estado = False
        self.prob = 0

    def cambiar_prob(self, prob):
        self.prob += prob
    
    def reiniciar_prob(self):
        self.prob = 0

    def cambiar_estado(self, estado):
        self.estado = estado


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


        
    
def simular(tablero, historial, tiempo):
    foco_inicial_x = random.randint(0, tablero.ancho-1)
    foco_inicial_y = random.randint(0, tablero.largo-1)
    tablero.mapa[foco_inicial_y][foco_inicial_x].cambiar_estado(True)
    viento = [random.randint(0,3)] + random.sample([-1, -1, -1, -1, 0, 1, 1, 1, 1], 2)
    tablero.viento = viento
    tablero.actualizar()
    historial.agregar(tablero)
    for t in range(1, tiempo):
        tablero.quemar()
        tablero.actualizar()
        historial.agregar(tablero)
    
    # transformar la entrada y salida a un formato "aplanado"
    foco_inicial = [foco_inicial_x, foco_inicial_y]
    tablero_inicial = [val for sublist in historial.historial[0] for val in sublist]
    tablero_final = [val for sublist in historial.historial[-1] for val in sublist]
    viento = tablero.viento
    tiempo = tiempo
    # agregar a un diccionario que representa una fila
    fila = {"foco_inicial_x": foco_inicial[0], "foco_inicial_y": foco_inicial[1],
            "tamaño_viento": viento[0], "viento_x": viento[1], "viento_y": viento[2],
            "tiempo": tiempo}
    for i in range(len(tablero_inicial)):
        fila["tablero_inicial_"+str(i)] = tablero_inicial[i]
        fila["tablero_final_"+str(i)] = tablero_final[i]
    return fila


if "__main__" == __name__:

    filas = []
    for _ in range(100):  # simular 100 veces
        tablero = Mapa(p.ANCHO_MAPA,p.LARGO_MAPA)
        historial = Historial()

        fila = simular(tablero, historial, 20)
        filas.append(fila)

    df = pd.DataFrame(filas)
    df.to_csv("simulacion3.csv", index=False)
