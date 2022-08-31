from Nodo import Nodo

class Cola:
    __pr = None
    __ul = None
    __cant = 0

    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def insertar(self, dato):
        ps1 = Nodo(dato)
        if self.__ul is None:
            self.__pr = ps1
        else:
            self.__ul.setSiguiente(ps1)
        self.__ul = ps1
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
        else:
            x = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr is None:
                self.__ul = None
            return x
