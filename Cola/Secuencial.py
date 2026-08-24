import numpy as np

class Cola:
    __pr: int
    __ul: int
    __max: int
    __cant: int
    __cola: np.ndarray

    def __init__(self, max): 
        self.__pr = 0
        self.__ul = 0
        self.__max = max
        self.__cant = 0
        self.__cola = np.empty(max, dtype = int)

    def estáLLena (self):
        return self.__cant == self.__max

    def estáVacia(self):
        return self.__cant == 0

    def Primero (self):
        return self.__pr

    def Ultimo (self):
        return self.__ul

    def Insertar (self, numerin):
        if not self.estáLLena():
            self.__cola[self.__ul] = numerin
            self.__ul = (self.__ul + 1) % self.__max
            self.__cant += 1
        else:
            print ("La cola está llena.")

    def Suprimir(self):
        if self.estáVacia():
            print ("La cola está vacía.")
        else:
            self.__cant -= 1
            print (f"se eliminó el numero {self.__cola[self.__pr]}.")
            self.__pr = (self.__pr + 1) % self.__max
            