# mapa.py
import numpy as np
import random

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