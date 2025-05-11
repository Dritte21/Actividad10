
# Patrón creacional: FACTORY METHOD
# -------------------------------
class Cita:
    def __init__(self, paciente, medico, fecha):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha

    def mostrar_info(self):
        return f"Cita para {self.paciente} con el Dr. {self.medico} el día {self.fecha}"

    def cambiar_medico(self, nuevo_medico):
        self.medico = nuevo_medico


class CitaFactory:
    @staticmethod
    def crear_cita(paciente, medico, fecha):
        return Cita(paciente, medico, fecha)


# -------------------------------
# Patrón estructural: DECORATOR
# -------------------------------
class CitaDecorator:
    def __init__(self, cita):
        self._cita = cita

    def mostrar_info(self):
        return self._cita.mostrar_info()


class CitaConRecordatorio(CitaDecorator):
    def mostrar_info(self):
        return self._cita.mostrar_info() + " [Recordatorio SMS activado]"


# -------------------------------
# Patrón de comportamiento: OBSERVER
# -------------------------------
class Sujeto:
    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensaje):
        for obs in self._observadores:
            obs.actualizar(mensaje)


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"[{self.nombre}] Notificación: {mensaje}")


# -------------------------------
# Interfaz de consola
# -------------------------------
def menu():
    print("\n=== Sistema de Citas Médicas ===")
    print("1. Agendar cita")
    print("2. Cambiar médico")
    print("3. Mostrar cita")
    print("4. Activar recordatorio SMS")
    print("5. Notificar usuarios")
    print("6. Salir")
    return input("Seleccione una opción: ")

if __name__ == "__main__":
    cita = None
    recordatorio_activado = False
    sistema = Sujeto()
    paciente_usuario = Usuario("Paciente")
    recepcionista_usuario = Usuario("Recepcionista")

    sistema.agregar_observador(paciente_usuario)
    sistema.agregar_observador(recepcionista_usuario)

    while True:
        opcion = menu()

        if opcion == "1":
            paciente = input("Ingrese nombre del paciente: ")
            medico = input("Ingrese nombre del médico: ")
            fecha = input("Ingrese fecha (dd/mm/aaaa): ")
            cita = CitaFactory.crear_cita(paciente, medico, fecha)
            recordatorio_activado = False
            print("Cita agendada correctamente.")

        elif opcion == "2":
            if cita:
                nuevo_medico = input("Ingrese nuevo médico: ")
                cita.cambiar_medico(nuevo_medico)
                print("Médico actualizado.")
            else:
                print("No hay cita registrada.")

        elif opcion == "3":
            if cita:
                if recordatorio_activado:
                    cita_decorada = CitaConRecordatorio(cita)
                    print(cita_decorada.mostrar_info())
                else:
                    print(cita.mostrar_info())
            else:
                print("No hay cita registrada.")

        elif opcion == "4":
            if cita:
                recordatorio_activado = True
                print("Recordatorio SMS activado.")
            else:
                print("No hay cita registrada.")

        elif opcion == "5":
            if cita:
                mensaje = "Su cita ha sido confirmada para el " + cita.fecha
                sistema.notificar(mensaje)
            else:
                print("No hay cita registrada.")

        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")