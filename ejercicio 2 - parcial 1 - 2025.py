from random import random, choice, expovariate, randint

class Cliente:
    __tiempoLLegada: int
    __siguiente: int

    def __init__(self, xtime):
        self.__tiempoLLegada = xtime
        self.__siguiente = None
        
    def getTiempoLL(self):
        return self.__tiempoLLegada

    def setTiempoLL(self, xtime):
        self.__tiempoLLegada = xtime

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, sig):
        self.__siguiente = sig

class Cajero:
    __pr: Cliente
    __ul: Cliente
    __cant: int
    __actual: Cliente

    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0
        self.__actual = None

    def vacía(self):
        return self.__cant == 0

    def Insertar(self, xtime):
        nuevo = Cliente(xtime)
        if self.vacía():
            self.__pr = nuevo
        else:
            self.__ul.setSiguiente(nuevo)
        self.__ul = nuevo
        self.__cant += 1

    def Suprimir(self):
        if self.vacía(): print("Cola vacía.")
        else:
            tiempito = self.__pr.getTiempoLL()
            aux = self.__pr
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr == None:
                self.__ul = None
            del aux
            return tiempito

    def Recorrer (self):
        if not self.vacía():
            self.__actual
            i = 0
            while self.__actual != None:
                print(f"{i} -> {self.__actual.getTiempoLL()}")
                self.__actual = self.__actual.getSiguiente()
                i += 1
        else: print("Cola vacía.")

    def getPr(self):
        return self.__pr

    def getUl(self):
        return self.__ul

    def getCantidadClientes(self):
        return self.__cant

if __name__ == '__main__':
    cajita1 = Cajero()
    cajita2 = Cajero()
    Cajas = [cajita1, cajita2]
    tiempoDeEspera = 0
    cantCliAtendidos = 0

    def Cajavacía():
        if Cajas[0].getCantidadClientes() > 0 and Cajas[1].getCantidadClientes() == 0: return 0
        elif Cajas[1].getCantidadClientes() > 0 and cajita1.getCantidadClientes() == 0: return 1
        elif cajita1.getCantidadClientes() > 0 and cajita2.getCantidadClientes() > 0: return choice(0,1)
        else: return None

    for i in range(240):
        if (i % 3 == 0):
            if randint(1,10) > 5:
                pass

