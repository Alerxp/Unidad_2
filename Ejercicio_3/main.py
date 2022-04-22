from os import system
from ManejadorRegistro import ManejadorRegistro

def menu():

    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Mostrar para cada variable el día y hora de menor y mayor valor")
        print("2. Indicar la temperatura promedio por cada hora")
        print("3. Valores de las variables por hora")
        print("4. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            variables = ["temperatura", "humedad", "presión atmosférica"]
            for i in range(len(variables)):
                diamenor = unMes.menorValor(variables[i])    # (dia, hora)
                diamayor = unMes.mayorValor(variables[i])    # (dia, hora)
                print("\nMenor {}: dia {}, hora {}".format(variables[i], diamenor[0], diamenor[1]))
                print("Mayor {}: dia {}, hora {}".format(variables[i], diamayor[0], diamayor[1]))
            system("pause")
        elif opc == 2:
            system("cls")
            print("\n|Hora|Temperatura promedio|")
            for i in range(24):
                print("{2}{0:>3} {2} {1:^19}{2}".format(i, unMes.tempPromedio(i), "|"))
            system("pause")
        elif opc == 3:
            system("cls")
            dia = int(input("\nIngrese un número de día: "))
            if dia in range(1, 31):
                unMes.mostrarDia(dia)
            else:
                print("\n*** El número ingresado no es válido ***")
            system("pause")
        elif opc == 4:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    unMes = ManejadorRegistro()
    unMes.testListaRegistros()
    menu()

