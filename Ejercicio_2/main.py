from os import system
from claseListaViajeros import ListaViajeros

def menu():
    viajero = listaViajeros.getViajero(num)
    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("Viajero seleccionao: {}\n".format(viajero))
        print("1. Consultar cantidad de millas")
        print("2. Acumular millas")
        print("3. Canjear millas")
        print("4. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            print("\nCantidad de millas: {}".format(viajero.cantidadTotaldeMillas()))
            system("pause")
        elif opc == 2:
            system("cls")
            millas = int(input("\nIngrese la cantidad de millas que acumuló: "))
            viajero.acumularMillas(millas)
            print("\nCantidad de millas actualizada: {}".format(viajero.cantidadTotaldeMillas()))
            system("pause")
        elif opc == 3:
            system("cls")
            millas = int(input("\nIngrese la cantidad de millas que desea canjear: "))
            viajero.canjearMillas(millas)
            system("pause")
        elif opc == 4:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    listaViajeros = ListaViajeros()
    listaViajeros.testListaViajeros()
    listaViajeros.mostrarViajeros()

    num = int(input("\nIngrese un número de viajero: "))
    if listaViajeros.isNumViajero(num):
        menu()
    else:
        print("\nEl número de viajero ingresado no existe")