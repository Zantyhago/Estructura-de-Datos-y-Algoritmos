import numpy as np

class Pila:
    dimension: int
    incremento: int
    cant: int
    pila: np.ndarray

    def __init__(self):
        self.cantidad = 0
        self.dimension = 6
        self.incremento = 3
        self.pila = np.empty(self.dimension, dtype = int)

    def agregarNum(self, numerito):
        if self.cant == self.dimension:
            self.dimension += self.incremento
            self.pila.resize(self.dimension)
        self.pila[self.cant] = numerito
        self.cant += 1
    
    def indice(self, valor):
        i = 0
        while i < self.cant and self.pila[i] != valor:
            i += 1
        return i

    def isVacia(self):
        return self.pila == 0
 
    def suprimir (self):
        if self.cant > 0:
            self.cant -= 1

    def longitud (self):
        return self.cant
    
    