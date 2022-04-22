import csv
from claseRegistro import Registro

class ManejadorRegistro:
    __listaRegistros = []

    def __init__(self):
        self.__listaRegistros = [[] for x in range(30)]

    def agregarRegistro(self, unRegistro, dia):
        if isinstance(unRegistro, Registro):
            self.__listaRegistros[dia - 1].append(unRegistro)

    def testListaRegistros(self):
        with open("abril.csv") as file:
            reader = csv.reader(file)
            next(file)
            for row in reader:
                dia = int(row[0])
                temp = int(row[2])
                hum = int(row[3])
                pre = float(row[4])
                unRegistro = Registro(temp, hum, pre)
                self.agregarRegistro(unRegistro, dia)

    def menorValor(self, variable):
        menor, dia, hora = 2000, 0, 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[0])):
                if variable == "temperatura":
                    aux = self.__listaRegistros[i][j].getTemperatura()
                elif variable == "humedad":
                    aux = self.__listaRegistros[i][j].getHumedad()
                elif variable == "presión atmosférica":
                    aux = self.__listaRegistros[i][j].getPresion()
                if aux < menor:
                    menor = aux
                    dia = i + 1
                    hora = j
        return dia, hora

    def mayorValor(self, variable):
        mayor, dia, hora = -100, 0, 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[0])):
                if variable == "temperatura":
                    aux = self.__listaRegistros[i][j].getTemperatura()
                elif variable == "humedad":
                    aux = self.__listaRegistros[i][j].getHumedad()
                elif variable == "presión atmosférica":
                    aux = self.__listaRegistros[i][j].getPresion()
                if aux > mayor:
                    mayor = aux
                    dia = i + 1
                    hora = j
        return dia, hora

    def tempPromedio(self, hora):
        acumTemp = 0
        for i in range(len(self.__listaRegistros)):
            acumTemp += self.__listaRegistros[i][hora].getTemperatura()
        return round(acumTemp / len(self.__listaRegistros), 1)

    def mostrarDia(self, dia):
        print("\n|Hora|Teperatura|Humedad|Presión|")
        for i in range(len(self.__listaRegistros[dia - 1])):
            print("{4}{0:>4}{4}{1:^10}{4}{2:^7}{4}{3:>7}{4}".format(i, self.__listaRegistros[dia - 1][i].getTemperatura(),
                                              self.__listaRegistros[dia - 1][i].getHumedad(),
                                              self.__listaRegistros[dia - 1][i].getPresion(), "|"))

    #def getRegistro(self, dia, hora):
    #    return self.__listaRegistros[dia - 1][hora]






