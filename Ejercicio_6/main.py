from claseListaViajeros import ListaViajeros

if __name__ == "__main__":
    viajeros = ListaViajeros()
    viajeros.testListaViajeros()

    v = viajeros.maxMillas()
    print("\n=== Viajero con mayor cantidad de millas ===\n", v)
    v += 100
    print("\n=== Acumula 100 millas ===\n", v)
    v -= 100
    print("\n=== Canjea 100 millas ===\n", v)
