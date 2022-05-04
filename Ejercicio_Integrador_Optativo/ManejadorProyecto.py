import csv
from claseProyecto import Proyecto

class ManejadorProyecto:

    def __init__(self):
        self.__proyectos = []

    def agregarProyecto(self, unProyecto):
        if type(unProyecto) == Proyecto:
            self.__proyectos.append(unProyecto)

    def testListaProyectos(self):
        with open("proyectos.csv") as file:
            reader = csv.reader(file, delimiter=";", skipinitialspace=True)
            next(file)
            for row in reader:
                id = row[0]
                titulo = row[1]
                palabras = row[2]
                unProyecto = Proyecto(id, titulo, palabras)
                self.agregarProyecto(unProyecto)

    def calculaPuntos(self, integrantes):
        for proyecto in self.__proyectos:

            minimo3 = integrantes.cantidadIntegrantes(proyecto.getProyecto())
            if minimo3:
                proyecto.acumulaPuntos(10)
            else:
                print("El Proyecto debe tener como mínimo 3 integrantes")
                proyecto.acumulaPuntos(-20)

            director, categoriaDirector = integrantes.tieneDirector(proyecto.getProyecto())
            if director:
                if categoriaDirector:
                    proyecto.acumulaPuntos(10)
                else:
                    print("El Director del Proyecto debe tener categoría I o II")
                    proyecto.acumulaPuntos(-5)
            else:
                print("El Proyecto debe tener un Director")
                proyecto.acumulaPuntos(-10)

            codirector, categoriaCodirector = integrantes.tieneCodirector(proyecto.getProyecto())
            if codirector:
                if categoriaCodirector:
                    proyecto.acumulaPuntos(10)
                else:
                    print("El Codirector del Proyecto debe tener como mínimo categoría III")
                    proyecto.acumulaPuntos(-5)
            else:
                print("El Proyecto debe tener un Codirector")
                proyecto.acumulaPuntos(-10)

            print(proyecto)
            print("-" * 71)

    def mostrarRankin(self):
        self.__proyectos.sort(reverse=True)
        for proyecto in self.__proyectos:
            print(proyecto)
            print("-" * 71)
