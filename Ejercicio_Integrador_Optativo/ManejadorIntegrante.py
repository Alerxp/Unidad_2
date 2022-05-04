import csv, numpy as np
from claseIntegrante import Integrante

class ManejadorIntegrante:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento = 5):
        self.__integrantes = np.empty(dimension, dtype=Integrante)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarIntegrante(self, unIntegrante):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__integrantes.resize(self.__dimension)
        self.__integrantes[self.__cantidad] = unIntegrante
        self.__cantidad += 1

    def testArregloIntegrantes(self):
        with open("integrantesProyecto.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                idProyecto = row[0]
                apellidoNombre = row[1]
                dni = row[2]
                categoria = row[3]
                rol = row[4]
                unIntegrante = Integrante(idProyecto, apellidoNombre, dni, categoria, rol)
                self.agregarIntegrante(unIntegrante)

    def cantidadIntegrantes(self, idProyecto):
        count, minimo3 = 0, False
        for i in range(self.__cantidad):
            if self.__integrantes[i].getProyecto() == idProyecto:
                count += 1
        if count >= 3:
            minimo3 = True
        return minimo3

    def tieneDirector(self, idProyecto):
        director = False
        categoria = False
        for i in range(self.__cantidad):
            if self.__integrantes[i].getProyecto() == idProyecto:
                if self.__integrantes[i].getRol() == "director":
                    director = True
                    if self.__integrantes[i].getCategoria() in ["I", "II"]:
                        categoria = True
                    break
        return director, categoria

    def tieneCodirector(self, idProyecto):
        codirector = False
        categoria = False
        for i in range(self.__cantidad):
            if self.__integrantes[i].getProyecto() == idProyecto:
                if self.__integrantes[i].getRol() == "codirector":
                    codirector = True
                    if self.__integrantes[i].getCategoria() in ["I", "II", "III"]:
                        categoria = True
                    break
        return codirector, categoria
