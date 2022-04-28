import csv
from os import system
from clasePlanAhorro import PlanAhorro

class ManejadorPlanAhorro:
    __planes = []

    def __init__(self):
        self.__planes = []

    def agregarPlan(self, plan):
        if isinstance(plan, PlanAhorro):
            self.__planes.append(plan)

    def testPlanes(self):
        with open("planes.csv") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                cod = row[0]
                mod = row[1]
                ver = row[2]
                val = int(row[3])
                unPlan = PlanAhorro(cod, mod, ver, val)
                self.agregarPlan(unPlan)

    def mostrarPlanes(self):
        print("|Código| Modelo |   Versión   | Valor |")
        for row in self.__planes:
            print(row)

    def actualizaPlanes(self):
        for plan in self.__planes:
            print(plan)
            valor = int(input("Ingrese el valor actual: "))
            plan.setValor(valor)
            print("=== Valor actualizado ===")
            print(plan)
            system("pause")

    def muestraSegunCuota(self, valor):
        print("\nLas cuotas de los siguientes vehículos son menores al valor ingresado: ")
        for plan in self.__planes:
            if plan.valorCuota() < valor:
                print(plan)

    def mostrarMontosLicitacion(self):
        print("")
        for plan in self.__planes:
            print("%s $%.2f" % (plan, plan.valorCuota() * PlanAhorro.getCuotasLicitacion()))
