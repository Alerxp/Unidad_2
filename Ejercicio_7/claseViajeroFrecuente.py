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
        return "Nro: {}, DNI: {}, Apellido y nombre: {} {}, Millas: {}".format(self.__num_viajero, self.__dni, self.__apellido, self.__nombre, self.__millas_acum)

    def __gt__(self, other):
        return self.__millas_acum > other.__millas_acum

    def __add__(self, millas):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + millas)

    def __sub__(self, millas):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - millas)

    def __eq__(self, millas):
        return self.__millas_acum == millas

    def __radd__(self, millas):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + millas)

    def __rsub__(self, millas):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - millas)
