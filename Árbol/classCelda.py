class Celda:
    __dato: int
    __der: object
    __izq: object

    def __init__(self, xdat):
        self.__dato = xdat
        self.__der = None
        self.__izq = None

    def getDato(self):
        return self.__dato

    def setDato(self, xdato):
        self.__dato = xdato

    def getDerecha(self):
        return self.__der

    def setDerecha(self, xder):
        self.__der = xder

    def getIzquierda(self):
        return self.__izq

    def setIzquierda(self, xizq):
        self.__izq = xizq