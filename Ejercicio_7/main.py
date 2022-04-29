from claseViajeroFrecuente import ViajeroFrecuente

if __name__ == "__main__":
    v = ViajeroFrecuente(10, "35507782", "Gabriela", "Balmaceda", 100)
    print("=== Datos del viajero ===\n", v)
    print("\n=== Compara 100 millas por izquierda ===")
    print("El viajero {}tiene 100 millas acumuladas".format("" if v == 100 else "no "))
    print("\n=== Compara 100 millas por derecha ===")
    print("El viajero {}tiene 100 millas acumuladas".format("" if 100 == v else "no "))
    v = 100 + v
    print("\n=== Acumula 100 millas por derecha ===\n{}".format(v))
    v = 100 - v
    print("\n=== Canjea 100 millas por derecha===\n{}".format(v))
