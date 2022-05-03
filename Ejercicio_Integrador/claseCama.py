class Cama:

    def __init__(self, id, hab, estado, paciente, diag, fechaIngreso, fechaSalida):
        self.__idCama = int(id)
        self.__habitacion = hab
        self.__estado = estado
        self.__nombrePaciente = paciente
        self.__diagnostico = diag
        self.__fechaInternacion = fechaIngreso
        self.__fechaAlta = fechaSalida

    def __str__(self):
        return "Paciente: {:<22} Cama: {:>2} Habitación: {:>3}\n" \
               "Diagnóstico: {:<14} Fecha de internación: {:<12}\n" \
               "Fecha de alta: {:<12}".format(self.__nombrePaciente, self.__idCama,
                                              self.__habitacion, self.__diagnostico,
                                              self.__fechaInternacion, self.__fechaAlta)

    def getNombre(self):
        return self.__nombrePaciente

    def getCama(self):
        return self.__idCama

    def setAlta(self, fecha):
        self.__fechaAlta = fecha

    def getEstado(self):
        return self.__estado

    def getDiagnostico(self):
        return self.__diagnostico
