from Cola import Cola

if __name__ == '__main__':
    c = Cola(3)
    c.insertar(1)        # Inserta el elemento 1 en la cola
    c.insertar(2)        # Inserta el elemento 2 en la cola
    c.insertar(3)        # Inserta el elemento 3 en la cola
    print(c.suprimir())  # Suprime el elemento 1 (primero en la cola), nuevo primer elemento 2
    c.insertar(4)        # Inserta el elemento 4 en la cola
    print(c.suprimir())  # Suprime el elemento 2 (primero en la cola), nuevo primer elemento 3
    c.insertar(0)        # Inserta el elemento 0 en la cola
    print(c.suprimir())  # Suprime el elemento 3 (primero en la cola), nuevo primer elemento 4
    print(c.suprimir())  # Suprime el elemento 4 (primero en la cola), nuevo primer elemento 0
    print(c.suprimir())  # Suprime el elemento 0, la cola queda vacía
    print(c.vacia())
