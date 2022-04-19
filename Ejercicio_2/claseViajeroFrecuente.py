class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    def __str__(self):
        return "Nro: {}, DNI: {}, Apellido y nombre: {}, {}".format(self.__num_viajero, self.__dni, self.__apellido, self.__nombre)
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def acumularMillas(self, acum_millas):
        self.__millas_acum += acum_millas
    def canjearMillas(self, canje_millas):
        if canje_millas <= self.cantidadTotaldeMillas():
            self.__millas_acum -= canje_millas
            print("\nSe canjearon {} millas".format(canje_millas))
        else:
            print("\n***Error***\nMillas insuficientes")
        self.cantidadTotaldeMillas()
    def numViajero(self):
        return self.__num_viajero