class Ventana:
    __titulo = ""
    __xL = 0
    __yL = 0
    __xR = 0
    __yR = 0

    def __init__(self, titulo, xL = 0, yL = 0, xR = 500, yR = 500):
        if xL >= 0 and yL >= 0 and xR <= 500 and yR <= 500 and xL < xR and yL < yR:
            self.__titulo = titulo
            self.__xL = xL
            self.__yL = yL
            self.__xR = xR
            self.__yR = yR

    def getTitulo(self):
        return self.__titulo

    def mostrar(self):
        print("Vértice superior izquierdo: ({}, {})".format(self.__xL, self.__yL))
        print("Vértice superior derecho: ({}, {})".format(self.__xR, self.__yR))

    def alto(self):
        return self.__xR - self.__xL

    def ancho(self):
        return self.__yR - self.__yL

    def moverDerecha(self, u = 1):
        self.__xL += u
        self.__xR += u

    def moverIzquierda(self, u = 1):
        self.__xL -= u
        self.__xR -= u

    def bajar(self, u = 1):
        self.__yL += u
        self.__yR += u

    def subir(self, u = 1):
        self.__yL -= u
        self.__yR -= u
