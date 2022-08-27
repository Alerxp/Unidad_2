from os import system
from Pila import Pila

def inicio(n):
    for i in range(n, 0, -1):
        p1.push(i)
    listaPilas.append(p1)
    listaPilas.append(p2)
    listaPilas.append(p3)

def fin():
    return p1.empty() and p2.empty() and p3.full()

def mostrarPilas():
    for i in range(len(listaPilas)):
        print("\nPila", i+1)
        listaPilas[i].show()

def mover(origen, destino):
    destino.push(origen.pop())

def nroPilaValido():
    origen = int(input("\nIngrese pila origen: "))
    while origen not in [1, 2, 3]:
        print("Error: sólo puede elegir Pila 1, 2, o 3")
        origen = int(input("\nIngrese pila origen: "))

    destino = int(input("Ingrese pila destino: "))
    destinos = [1, 2, 3]
    destinos.remove(origen)
    while destino not in destinos:
        print("Error: el número de pila destino no es válido")
        destino = int(input("\nIngrese pila destino: "))
    return origen, destino

def movimientoValido():
    dato = nroPilaValido()
    pilaOrigen = listaPilas[dato[0]-1]
    pilaDestino = listaPilas[dato[1]-1]
    if not pilaOrigen.empty():
        if not pilaDestino.full():
            if pilaDestino.empty() or pilaOrigen.getDato() < pilaDestino.getDato():
                mover(pilaOrigen, pilaDestino)
                global cant
                cant += 1
            else:
                print("Error: sólo puede apilar una pieza encima de una más grande")
                system('pause')
        else:
            print("La pila destino está llena")
    else:
        print("La pila origen está vacía")
    mostrarPilas()
    print("\n" + "-" * 29)

if __name__ == '__main__':
    print("****** TORRES DE HANOI ******")
    n = int(input("Ingrese cantidad de discos: "))
    p1 = Pila(n)
    p2 = Pila(n)
    p3 = Pila(n)
    listaPilas = []
    cant = 0

    inicio(n)
    mostrarPilas()
    while not fin():
        movimientoValido()
    mostrarPilas()

    print("\n¡Buen trabajo!")
    print("Terminaste en", cant, "movimientos")
    print("Número mínimo de movimientos:", 2**n - 1)
