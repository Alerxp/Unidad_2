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

    def unstack(self, n):
        if self.empty():
            print("Pila vacía")
        else:
            f = self.__tope.getDato()
            aux = self.__tope
            while aux is not None:
                f *= self.pop().getDato()
                aux = aux.getSiguiente()
            print(f"Factorial de {n}: {f}")

    def factorial(self, n):
        if n < 0:
            print("El número deber ser mayor o igual a 0")
        elif n == 0:
            print(f"Factorial de {n}: 1")
        else:
            for i in range(n, 0, -1):
                self.push(i)
            return self.unstack(n)
