from classNodo import Nodo

class GestorLista:
    comienzo: Nodo
    actual: Nodo
    tope: int
    indice: int
    
    def __init__(self):
        self.comienzo = None
        self.actual = None
        self.tope = 0
        self.indice = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice == self.tope:
            self.actual = self.comienzo
            self.indice = 0
            raise StopIteration
        else:
            dato = self.actual.getDato()
            self.indice += 1
            self.actual = self.actual.getSiguiente()
            return dato

    def agregaVehiculo(self, numerito):
        nodo = Nodo(numerito)
        nodo.setSiguiente(self.comienzo)
        self.comienzo = nodo
        self.tope += 1
        self.actual = nodo

    