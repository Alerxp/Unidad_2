from os import system
from clasePlanAhorro import PlanAhorro
from ManejadorPlanAhorro import ManejadorPlanAhorro

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Actualizar valores de vehículos")
        print("2. Mostrar vehículos según valor de cuota")
        print("3. Mostrar el monto pagado para licitar")
        print("4. Modificar cantidad de cuotas para licitar")
        print("5. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            planes.actualizaPlanes()
            system("pause")
        elif opc == 2:
            system("cls")
            valor = int(input("\nIngrese el valor de la cuota que puede pagar: "))
            planes.muestraSegunCuota(valor)
            system("pause")
        elif opc == 3:
            system("cls")
            planes.mostrarMontosLicitacion()
            system("pause")
        elif opc == 4:
            system("cls")
            cuotas = int(input("\nIngrese cantidad de cuotas: "))
            PlanAhorro.cuotasLicitacion = cuotas
            print("\nCantidad actual de cuotas pagas para licitar: {}".format(PlanAhorro.getCuotasLicitacion()))
            system("pause")
        elif opc == 5:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    planes = ManejadorPlanAhorro()
    planes.testPlanes()
    planes.mostrarPlanes()
    menu()
