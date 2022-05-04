class Proyecto:

    def __init__(self, id, titulo, palabras):
        self.__idProyecto = id
        self.__titulo = titulo
        self.__palabrasClave = palabras
        self.__puntos = 0

    def getProyecto(self):
        return self.__idProyecto

    def acumulaPuntos(self, puntos):
        self.__puntos += puntos

    def __str__(self):
        return "id: {}\nTítulo: {}\nPalabras claves: {}\nPuntos: {}".format(self.__idProyecto, self.__titulo, self.__palabrasClave, self.__puntos)

    def __gt__(self, other):
        return self.__puntos > other.__puntos
