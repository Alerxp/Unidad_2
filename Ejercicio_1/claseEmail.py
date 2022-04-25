import re

class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __password = ""
    def __init__(self, idCuenta, dominio, tipoDominio, password):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__password = password
    def retornaEmail(self):
        return "{}@{}.{}".format(self.__idCuenta, self.__dominio, self.__tipoDominio)
    def getDominio(self):
        return self.__dominio
    def crearCuenta(email):
        if re.match('(^[a-z0-9]+.[^ ]*)@(gmail|hotmail|outlook|yahoo)\.(com|es)', email.lower()):
            print("\nCorreo válido")
            aux1 = email.split("@")
            aux2 = aux1[1].split(".")
            idCuenta = aux1[0]
            dominio = aux2[0]
            tipoDominio = aux2[1]
            password = input("Ingrese su contraseña: ")
            otroemail = Email(idCuenta, dominio, tipoDominio, password)
            print("\nNueva cuenta: {}".format(otroemail.retornaEmail()))
        else:
            print("\nCorreo no válido")
    def changePassword(self, oldpassword):
        while self.__password != oldpassword:
            print("\nContraseña incorrecta")
            oldpassword = input("Ingrese su contraseña actual: ")
        newpassword = input("\nIngrese su nueva contraseña: ")
        self.__password = newpassword
        print("Su contraseña se cambió correctamente")