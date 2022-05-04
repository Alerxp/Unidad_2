class Integrante:

    def __init__(self, idProyecto, apellidoNombre, dni, categoria, rol):
        self.__idProyecto = idProyecto
        self.__apellidoNombre = apellidoNombre
        self.__dni = dni
        self.__categoria = categoria
        self.__rol = rol

    def getProyecto(self):
        return self.__idProyecto

    def getRol(self):
        return self.__rol

    def getCategoria(self):
        return self.__categoria
