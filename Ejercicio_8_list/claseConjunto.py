class Conjunto:

    def __init__(self):
        self.__set = []

    def __str__(self):
        set = ""
        for n in self.__set:
            set += str(n) + ", "
        return "{" + set[:-2] + "}"

    def agregarElementos(self, numbers):
        # numbers.sort()
        for n in numbers:
            if type(n) == int and n not in self.__set:
                self.__set.append(n)

    def __add__(self, other):
        C = Conjunto()
        C.agregarElementos(self.__set)
        C.agregarElementos(other.__set)
        # C.__set.sort()
        return C

    def __sub__(self, other):
        C = Conjunto()
        A = self.__set
        B = other.__set
        sub = []
        for n in A:
            if n not in B:
                sub.append(n)
        C.agregarElementos(sub)
        return C

    def __eq__(self, other):
        A = self.__set
        B = other.__set
        are_equal = True
        if len(A) == len(B):
            i = 0
            while i < len(A) and A[i] in B:
                i += 1
            if i != len(A):
                are_equal = False
        else:
            are_equal = False
        return are_equal
