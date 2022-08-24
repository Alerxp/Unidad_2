from Pila import Pila

if __name__ == '__main__':
    p = Pila()
    d = int(input("Ingrese un número: "))
    p.decimalToBinary(d)
    print(f"{d} en binario: {p.unstack()}")
