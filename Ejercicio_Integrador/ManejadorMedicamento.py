import csv
from claseMedicamento import Medicamento

class ManejadorMedicamento:

    def __init__(self):
        self.__medicamentos = []

    def agregarMedicamento(self, unMedicamento):
        if type(unMedicamento) == Medicamento:
            self.__medicamentos.append(unMedicamento)

    def testListaMedicamentos(self):
        with open("medicamentos.csv") as file:
            reader = csv.reader(file, delimiter=";")
            next(file)
            for row in reader:
                idCama = row[0]
                idMed = row[1]
                nombre = row[2]
                droga = row[3]
                presentacion = row[4]
                cantidad = row[5]
                precio = row[6]
                unMedicamento = Medicamento(idCama, idMed, nombre, droga, presentacion, cantidad, precio)
                self.agregarMedicamento(unMedicamento)

    def mostrarMedicamentos(self, idCama):
        total = 0
        for medicamento in self.__medicamentos:
            if medicamento.getidCama() == idCama:
                total += medicamento.getPrecio()
                print(medicamento)
        return total
