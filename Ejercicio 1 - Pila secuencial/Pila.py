class Pila:
    __items = []
    __tope = -1
    __max = 3

    def __init__(self, max=3):
        self.__items = []
        self.__tope = -1
        self.__max = max

    def __str__(self):
        return f"{self.__items}"

    def empty(self):
        return self.__tope == -1

    def full(self):
        return self.__tope == self.__max-1

    def push(self, x):
        if not self.full():
            self.__tope += 1
            self.__items.insert(self.__tope, x)
        else:
            print("Pila llena")

    def pop(self):
        if not self.empty():
            x = self.__items[self.__tope]
            self.__tope -= 1
            return x
        else:
            print("Pila vacía")

    def unstack(self):
        if not self.empty():
            for i in range(self.__tope, -1, -1):
                print(self.pop())
        else:
            print("Pila vacía")
