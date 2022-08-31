from Cola import Cola
from random import random

if __name__ == '__main__':
    c = Cola()
    cliente = 0
    cajero = 0
    tec = 0      # tiempo de espera del cliente
    # tea = 0    # tiempo de espera acumulado
    reloj = 0
    cca = 0      # cantidad de clientes atendidos
    temax = 0    # tiempo de espera máximo
    print("****** COMIENZA SIMULACION ******\n")
    tms = int(input("Tiempo máximo de simulación: "))
    x = int(input("Frecuencia de llegada de clientes: "))
    y = int(input("Tiempo de atención del cajero: "))

    while reloj != tms:
        n = round(random(), 1)  # número del intervalo [0.0, 1.0) truncado a una cifra decimal
        if n <= 1/x:
            c.insertar(reloj)
        if cajero == 0:
            if not c.vacia():
                cliente = c.suprimir()
                tec = reloj - cliente
                # tea += tec
                cca += 1
                cajero = y
                if tec > temax:
                    temax = tec
        reloj += 1
        if cajero > 0:
            cajero -= 1

    print("\n***** SIMULACION FINALIZADA *****\n")
    print(f"En {tms} se atendieron {cca} clientes")
    print(f"El tiempo máximo de espera fue {temax} minutos")
