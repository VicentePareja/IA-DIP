import numpy as np
import random

class Mapa:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        self.mapa = [[0 for i in range(ancho)] for j in range(largo)]
        self.viento = [0,0,0]

    def actualizar(self):
        for i in range(self.largo):
            for j in range(self.ancho):
                if self.mapa[i][j].estado:
                    try:
                        prob = random.randint(0,25)/100
                        self.mapa[i][abs(j+1)].cambiar_prob(prob)

                    except:
                        pass

                    try:
                        prob = random.randint(0,25)/100
                        self.mapa[i][abs(j-1)].cambiar_prob(prob)
                    except:
                        pass

                    try:
                        prob = random.randint(0,25)/100
                        self.mapa[abs(i+1)][j].cambiar_prob(prob)
                    except:
                        pass

                    try:
                        prob = random.randint(0,25)/100
                        self.mapa[abs(i-1)][j].cambiar_prob(prob)
                    except: 
                        pass

                    
                    for _ in range(1, self.viento[0] + 1):
                        try:
                            self.mapa[i][abs(j + self.viento[2]*_)].cambiar_prob((self.viento[0] + 1 -_)*prob)
                        except: 
                            pass

                        try:
                            self.mapa[abs(i + self.viento[1]*_)][j].cambiar_prob((self.viento[0] + 1 -_)*prob)
                        except: 
                            pass


    def quemar(self):
        for i in range(self.largo):
            for j in  range(self.ancho):
                aux = random.random()
                if aux <= self.mapa[i][j].prob:
                    self.mapa[i][j].cambiar_estado(True)
                self.mapa[i][j].reiniciar_prob()


                



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
        aux = [[0 for i in range(len(mapa[0]))] for j in range(len(mapa))]
        for i in range(len(mapa)):
            for j in range(len(mapa[0])):
                if mapa[i][j].estado:
                    aux[i][j] = 1000
                else:
                    aux[i][j] = mapa[i][j].prob*100//1
        self.historial.append(aux)
        
    
def simular(tablero, historial):
    foco_inicial_x = random.randint(0, tablero.ancho-1)
    foco_inicial_y = random.randint(0, tablero.largo-1)
    tablero.mapa[foco_inicial_y][foco_inicial_x].cambiar_estado(True)
    viento = [random.randint(0,3)] + random.sample([-1, -1, -1, -1, 0, 1, 1, 1, 1], 2)
    tablero.viento = viento
    tablero.actualizar()
    historial.agregar(tablero.mapa)
    for t in range(1,20):
        tablero.quemar()

        tablero.actualizar()
        historial.agregar(tablero.mapa)
    return historial

tablero = Mapa(30,30)
historial = Historial()

for i in range(tablero.largo):
    for j in range(tablero.ancho):
        tablero.mapa[i][j] = Casilla()
    
a = simular(tablero, historial)



for i in range(len(a.historial)):
    matriz = np.array(a.historial[i])

    np.savetxt("matriz_bonita.txt", matriz, fmt="%4d")
    with open("matriz_bonita.txt", "r") as file:
        print(file.read())

    

    
        
    






    



