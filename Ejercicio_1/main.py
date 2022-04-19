from claseEmail import Email
import csv

if __name__ == "__main__":
    print("*****BIENVENIDO*****")
    nombre = input("Ingrese su nombre: ")
    idCuenta = input("Ingrese id de su cuenta: ")
    dominio = input("Ingrese dominio de su cuenta: ")
    tipoDominio = input("Ingrese el tipo de dominio de su cuenta: ")
    password = input("Ingrese su contraseña: ")
    email1 = Email(idCuenta, dominio, tipoDominio, password)
    print("\nEstimado {} te enviaremos tus mensajes a la dirección {}".format(nombre, email1.retornaEmail()))

    changepassword = input("\n¿Desea cambiar su contraseña? si/no: ")
    if changepassword.lower() == "si":
        print("\n*****MODIFICAR CONTRASEÑA*****")
        oldpassword = input("\nIngrese la contraseña actual: ")
        email1.changePassword(oldpassword)

    print("\n*****CREAR NUEVA CUENTA*****")
    email = input("\nIngrese la dirección de la nueva cuenta: ")
    Email.crearCuenta(email)

    print("\n*****ARCHIVO DE CORREOS*****")
    with open("correos.csv") as file:
        reader = csv.reader(file, delimiter=';')

        idCuentas = []
        for row in reader:
            idCuentas.append(row[0])
            Email.crearCuenta(row[0]+row[1]+row[2]+'.'+row[3])

    id = input("\nIngrese un idCuenta: ")
    if id in idCuentas:
        print("\nEl idCuenta {}está repetido".format("" if idCuentas.count(id) > 1 else "no "))
    else:
        print("\nEl identificador ingresado no se encuentra en el archivo")