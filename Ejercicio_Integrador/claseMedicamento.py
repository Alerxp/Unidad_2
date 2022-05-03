class Medicamento:

    def __init__(self, idCama, idMed, nombre, droga, presentacion, cantidad, precio):
        self.__idCama = int(idCama)
        self.__idMedicamento = idMed
        self.__nombreComercial = nombre
        self.__monodroga = droga
        self.__presentacion = presentacion
        self.__cantidadAplicada = cantidad
        self.__precioTotal = int(precio)

    def __str__(self):
        return "{:>12}/{:<15} {:^19} {:>5} {:>12}".format(self.__nombreComercial, self.__monodroga, self.__presentacion,
                                       self.__cantidadAplicada, self.__precioTotal)

    def getidCama(self):
        return self.__idCama

    def getPrecio(self):
        return self.__precioTotal
