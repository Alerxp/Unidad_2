class Conjunto:

    def __init__(self):
        self.__set = set()

    def __str__(self):
        return f"{self.__set}"

    def agregarElementos(self, numbers):
        """
        n not in self.__set --> No es necesario
        El tipo de dato set() no admite elementos repetidos
        """
        for n in numbers:
            if type(n) == int:
                self.__set.add(n)

    def __add__(self, other):
        C = Conjunto()
        C.agregarElementos(self.__set | other.__set)    # Unión de conjuntos .union()
        return C

    def __sub__(self, other):
        C = Conjunto()
        C.agregarElementos(self.__set - other.__set)    # Diferencia de conjuntos .difference()
        return C

    def __eq__(self, other):
        return self.__set == other.__set    # Igualdad de conjuntos
