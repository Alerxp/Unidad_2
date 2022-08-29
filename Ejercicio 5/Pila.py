class Pila:
    __items = []
    __tope = -1
    __max = 3

    def __init__(self, max=3):
        self.__items = [0 for _ in range(max)]
        self.__tope = -1
        self.__max = max

    def empty(self):
        return self.__tope == -1

    def full(self):
        return self.__tope == self.__max-1

    def push(self, x):
        if not self.full():
            self.__tope += 1
            self.__items[self.__tope] = x
        else:
            print("Pila llena")

    def pop(self):
        if not self.empty():
            x = self.__items[self.__tope]
            self.__tope -= 1
            return x
        else:
            print("Pila vacía")

    def show(self):
        if self.empty():
            print("Vacía")
        else:
            for i in range(self.__tope, -1, -1):
                blanks = i
                print(" "*(blanks+1) + "_"*(self.__items[i]*2-1) + " "*(blanks+1))
                print(" "*blanks + "|" + " "*(self.__items[i]-1) + str(self.__items[i])
                      + " "*(self.__items[i]-1) + "|" + " "*blanks)

    def getDato(self):
        return self.__items[self.__tope]
