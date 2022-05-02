import csv, numpy as np
from claseCama import Cama

class ManejadorCama:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__camas = np.empty(dimension, dtype=Cama)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarCama(self, unaCama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = unaCama
        self.__cantidad += 1

    def testArregloCamas(self):
        with open("camas.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                id = row[0]
                hab = row[1]
                estado = row[2]
                paciente = row[3]
                diag = row[4]
                fechaIngreso = row[5]
                fechaSalida = row[6]
                unaCama = Cama(id, hab, estado, paciente, diag, fechaIngreso, fechaSalida)
                self.agregarCama(unaCama)

    def burcarNombre(self, nombre):
        i = 0
        while(i < self.__cantidad):
            if self.__camas[i].getNombre() == nombre:
                break
            else:
                i += 1
        if i < self.__cantidad:
            return self.__camas[i].getCama()
        else:
            return -1

    def getPaciente(self, idCama):
        return self.__camas[idCama - 1]

    def mostrarPacientes(self, diagnostico):
        for paciente in self.__camas:
            if paciente.getEstado() and paciente.getDiagnostico() == diagnostico:
                paciente.setAlta("")
                print(paciente)
