from os import system
from claseConjunto import Conjunto

def menu():
    while True:
        print("\n***** MENÚ DE OPCIONES *****\n")
        print("1. Unión")
        print("2. Diferencia")
        print("3. Igualdad")
        print("4. Salir")
        opc = int(input("\nIngrese una OPCIÓN: "))
        if opc == 1:
            system("cls")
            print("A + B =", A + B)
            system("pause")
        elif opc == 2:
            system("cls")
            print("A - B =", A - B)
            system("pause")
        elif opc == 3:
            system("cls")
            print("A = B --> {}".format("Verdadero" if A == B else "Falso"))
            system("pause")
        elif opc == 4:
            break
        else:
            print("\nOPCIÓN INCORRECTA")
            system("pause")
        system("cls")

if __name__ == "__main__":
    print("=== CONJUNTOS ===")
    A = Conjunto()
    B = Conjunto()
    A.agregarElementos([1, 2, 3, 4])
    B.agregarElementos([3, 6, 9])
    print("A =", A)
    print("B =", B)
    system("pause")
    menu()
