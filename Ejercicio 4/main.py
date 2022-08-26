from Pila import Pila

if __name__ == '__main__':
    p = Pila()
    print(p.empty(1))  # Pila1 vacía
    print(p.empty(2))  # Pila2 vacía
    p.push(1, 3)       # Apila el elemento 3 en la Pila1
    p.push(1, 1)       # Apila el elemento 1 en la Pila1
    p.push(2, 5)       # Apila el elemento 5 en la Pila2
    p.push(2, 7)       # No se puede apilar, Pila llena
    print(p.full())    # Pila llena
