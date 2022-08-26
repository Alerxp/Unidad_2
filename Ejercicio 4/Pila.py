class Pila:
    __items = []
    __max = 3
    __tope1 = -1
    __tope2 = 3

    def __init__(self, max=3):
        self.__items = []
        self.__tope1 = -1
        self.__tope2 = max
        self.__max = max

    def __str__(self):
        return f"{self.__items}"

    def empty(self, pila):
        rta = None
        if pila == 1:
            rta = self.__tope1 == -1
        elif pila == 2:
            rta = self.__tope2 == self.__max
        return rta

    def full(self):
        return self.__tope1 + 1 == self.__tope2

    def push(self, pila, x):
        if not self.full():
            if pila == 1:
                self.__tope1 += 1
                self.__items.insert(self.__tope1, x)
            elif pila == 2:
                self.__tope2 -= 1
                self.__items.insert(self.__tope2, x)
        else:
            print(f"Pila llena")

    def pop(self, pila):
        if not self.empty(pila) and pila == 1:
            x = self.__items[self.__tope1]
            self.__tope1 -= 1
            return x
        elif not self.empty(pila) and pila == 2:
            x = self.__items[self.__tope2]
            self.__tope1 += 1
            return x
        else:
            print("Pila vacía")
