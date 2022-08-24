from Pila import Pila

if __name__ == '__main__':
    p = Pila()
    print(p.empty())  # Pila vacía
    p.push(3)
    p.push(1)
    p.push(5)         # Pila llena
    p.push(7)         # No se puede apilar
    p.unstack()       # Desapilar
    print(p.empty())  # Pila vacía
