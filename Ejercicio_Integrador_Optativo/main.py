from ManejadorProyecto import ManejadorProyecto
from ManejadorIntegrante import ManejadorIntegrante

if __name__ == "__main__":
    listaProyectos = ManejadorProyecto()
    listaProyectos.testListaProyectos()
    arregloIntegrantes = ManejadorIntegrante(5)
    arregloIntegrantes.testArregloIntegrantes()
    print("=" * 30, "PROYECTOS", "=" * 30)
    listaProyectos.calculaPuntos(arregloIntegrantes)
    input("Presione una tecla para ver el rankin de Proyectos por puntaje...")
    print("=" * 31, "RANKIN", "=" * 32)
    listaProyectos.mostrarRankin()
