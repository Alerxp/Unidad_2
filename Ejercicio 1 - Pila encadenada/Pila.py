from Nodo import Nodo

class Pila:
    __tope = None

    def __init__(self):
        self.__tope = None

    def empty(self):
        return self.__tope is None

    def push(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__tope)
        self.__tope = nodo

    def pop(self):
        if self.empty():
            print("Pila vacía")
        else:
            aux = self.__tope
            self.__tope = aux.getSiguiente()
            return aux

    def unstack(self):
        if self.empty():
            print("Pila vacía")
        else:
            aux = self.__tope
            while aux is not None:
                print(self.pop().getDato())
                aux = aux.getSiguiente()
