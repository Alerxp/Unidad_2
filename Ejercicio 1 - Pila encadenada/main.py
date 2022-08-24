from Pila import Pila

if __name__ == '__main__':
    p = Pila()
    print(p.empty())  # Pila vacía
    p.push(3)
    p.push(1)
    p.push(5)
    p.unstack()       # Desapilar
    print(p.empty())  # Pila vacía
