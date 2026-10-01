from classCelda import Celda

class Arbol:
    __raíz: Celda

    def __init__(self):
        self.__raíz = None

    def vacía(self):
        return self.__raíz == None

    def Grado(self, nodo):
            grado = 0
            if nodo.getIzquierda():
                grado += 1
            if nodo.getDerecha():
                grado += 1
            return grado

    def Insertar(self, elemento):
        if self.vacía():
            self.__raíz = Celda(elemento)
            print(f"Raíz creada con el elemento {elemento}.")
        else:
            self.InsertarIzqDer(self.__raíz, elemento)       

    def InsertarIzqDer(self, celda, elemento):
        if celda.getDato() == elemento:
            print(f"{elemento} ya ha sido insertado.")
        elif elemento < celda.getDato():
            if celda.getIzquierda():
                self.InsertarIzqDer(celda.getIzquierda(), elemento)
            else:
                celda.setIzquierda(Celda(elemento))
        else:
            if celda.getDerecha():
                self.InsertarIzqDer(celda.getDerecha(), elemento)
            else:
                celda.setDerecha(Celda(elemento))

    def Suprimir(self, valor):
        self.__raíz = self.EliminaNodo(self.__raíz, valor)

    def EliminaNodo(self, nodo, valor):
        if not nodo: return None
        elif nodo.getDato() > valor:
            nodo.setIzquierda(self.EliminaNodo(nodo.getIzquierda(), valor))
        elif nodo.getDato() < valor:
            nodo.setDerecha(self.EliminaNodo(nodo.getDerecha(), valor))
        else:
            if self.grado(nodo) == 0:
                return None
            elif self.grado(nodo) == 1:
                if nodo.getDerecha():
                    return nodo.getDerecha()
                else:
                    return nodo.getIzquierda()
            elif self.grado(nodo) == 2:
                maximo = nodo.getIzquierda()
                while maximo != None:
                    maximo = maximo.getDerecha()
                nodo.setDato(maximo.getDato())
                nodo.setIzquierda(self.EliminaNodo(nodo.getIzquierda(), maximo.getDato()))

    def CantNodos(self):
        if self.vacía():
            print("Árbol vacío.")
        else:
            cant = 1
            cant += self.CuentaNodos(self.__raíz, cant)
            print(f"cantidad de nodos: {cant}")

    def CuentaNodos(self, nodo, cant):
        '''if nodo:
            cant += 1'''
        if nodo.getDerecha():
            cant += self.CuentaNodos(nodo.getDerecha(), cant)
            #cant += 1
        if nodo.getIzquierda():
            cant += self.CuentaNodos(nodo.getIzquierda(), cant)
        return cant
        print(f"cantidad de nodos: {cant}")

if __name__ == '__main__':
    arbolito = Arbol()
    arbolito.Insertar(50)
    arbolito.Insertar(10)
    arbolito.Insertar(60)
    arbolito.Insertar(70)
    arbolito.Insertar(20)
    #arbolito.Suprimir(70)
    arbolito.CantNodos()