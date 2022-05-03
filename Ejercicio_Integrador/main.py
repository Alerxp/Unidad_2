from os import system
from ManejadorCama import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento

if __name__ == "__main__":
    arregloCamas = ManejadorCama(3)
    arregloCamas.testArregloCamas()
    listaMedicamentos = ManejadorMedicamento()
    listaMedicamentos.testListaMedicamentos()

    print("\n========================= ALTA DE PACIENTE =========================\n")
    nombre = input("Ingrese apellido y nombre del paciente: ")
    idCama = arregloCamas.burcarNombre(nombre)
    if idCama == -1:
        print("\nNo se encontró un paciente con ese nombre")
    else:
        unPaciente = arregloCamas.getPaciente(idCama)
        unPaciente.setAlta("2/5/2021")
        print(unPaciente)
        print("\n Medicamento/monodroga          Presentación     Cantidad     Precio")
        total = listaMedicamentos.mostrarMedicamentos(idCama)
        print(" Total adeudado: {:>50}".format(total))
        system("pause")

    print("===================== PACIENTES POR DIAGNOSTICO =====================\n")
    diagnostico = input("Ingrese un diagnostico: ")
    arregloCamas.mostrarPacientes(diagnostico)
