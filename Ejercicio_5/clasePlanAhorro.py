class PlanAhorro:
    # variables de clase
    cuotasPlan = 60
    cuotasLicitacion = 10

    def __init__(self, cod, mod, ver, val):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = val

    def __str__(self):
        return "|{:^6}|{:<8}|{:<13}|{:>7}|".format(self.__codigo, self.__modelo, self.__version, self.__valor)

    def setValor(self, valor):
        self.__valor = valor

    def valorCuota(self):
        return float(self.__valor) * 1.1 / PlanAhorro.cuotasPlan

    @classmethod
    def getCuotasLicitacion(cls):
        return cls.cuotasLicitacion
