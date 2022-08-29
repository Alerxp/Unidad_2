class Cola:
    __items = []
    __pr = 0
    __ul = 0
    __cant = 0
    __max = 3

    def __init__(self, max=3):
        self.__pr = 0
        self.__ul = 0
        self.__cant = 0
        self.__max = max
        self.__items = [None for _ in range(max)]

    def vacia(self):
        return self.__cant == 0

    def insertar(self, x):
        if self.__cant < self.__max:
            self.__items[self.__ul] = x
            self.__ul = (self.__ul+1) % self.__max
            self.__cant += 1
        else:
            print("Cola llena")

    def suprimir(self):
        if not self.vacia():
            x = self.__items[self.__pr]
            self.__pr = (self.__pr+1) % self.__max
            self.__cant -= 1
            return x
        else:
            print("Cola vacía")
