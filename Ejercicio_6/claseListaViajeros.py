import csv
from claseViajeroFrecuente import ViajeroFrecuente

class ListaViajeros:
    __viajeros = []

    def __init__(self):
        self.__viajeros = []

    def agregarViajero(self, viajero):
        if isinstance(viajero, ViajeroFrecuente):
            self.__viajeros.append(viajero)

    def testListaViajeros(self):
        with open("viajeros.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)    # Omite encabezado
            for row in reader:
                num_viajero = int(row[0])
                dni = row[1]
                nombre = row[2]
                apellido = row[3]
                millas_acum = int(row[4])
                unViajero = ViajeroFrecuente(num_viajero, dni, nombre, apellido, millas_acum)
                self.agregarViajero(unViajero)

    def maxMillas(self):
        return max(self.__viajeros)
