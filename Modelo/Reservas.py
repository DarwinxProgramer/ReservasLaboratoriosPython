import pickle

class ModeloReservas:
    def __init__(self, archivo_reservas_aprobadas='reservas_aprobadas.dat', archivo_reservas_pendientes='reservas_pendientes.dat'):
        self.reservas_aprobadas = []
        self.reservas_pendientes = []
        self.reservas_rechazadas = []
        self.archivo_reservas_aprobadas = archivo_reservas_aprobadas
        self.archivo_reservas_pendientes = archivo_reservas_pendientes
        self.cargar_reservas_aprobadas()
        self.cargar_reservas_pendientes()

    def realizar_reserva(self, laboratorio, fecha, hora, rol, estado="pendiente"):
        reserva = {'laboratorio': laboratorio, 'fecha': fecha, 'hora': hora, 'rol': rol, 'estado': estado}
        self.reservas_pendientes.append(reserva)
        self.guardar_reservas_pendientes()

    def guardar_reservas_aprobadas(self):
        data = {
            'reservas_aprobadas': self.reservas_aprobadas,
        }

        with open(self.archivo_reservas_aprobadas, 'wb') as file:
            pickle.dump(data, file)

    def cargar_reservas_aprobadas(self):
        try:
            with open(self.archivo_reservas_aprobadas, 'rb') as file:
                data = pickle.load(file)
                self.reservas_aprobadas = data.get('reservas_aprobadas', [])
        except FileNotFoundError:
            pass
        except (pickle.UnpicklingError, MemoryError) as e:
            print(f"Error al cargar reservas aprobadas: {e}")

    def guardar_reservas_pendientes(self):
        data = {
            'reservas_pendientes': self.reservas_pendientes,
        }

        with open(self.archivo_reservas_pendientes, 'wb') as file:
            pickle.dump(data, file)

    def cargar_reservas_pendientes(self):
        try:
            with open(self.archivo_reservas_pendientes, 'rb') as file:
                data = pickle.load(file)
                self.reservas_pendientes = data.get('reservas_pendientes', [])
        except FileNotFoundError:
            pass
        except (pickle.UnpicklingError, MemoryError) as e:
            print(f"Error al cargar reservas pendientes: {e}")
    def aprobar_reserva(self, indice_reserva):
        if 0 <= indice_reserva < len(self.reservas_pendientes):
            reserva = self.reservas_pendientes.pop(indice_reserva)
            reserva['estado'] = 'Aprobada'
            self.reservas_aprobadas.append(reserva)
            self.guardar_reservas_aprobadas()
            self.guardar_reservas_pendientes()  # Se guarda la lista actualizada de reservas pendientes

    def rechazar_reserva(self, indice_reserva):
        if 0 <= indice_reserva < len(self.reservas_pendientes):
            reserva = self.reservas_pendientes.pop(indice_reserva)
            reserva['estado'] = 'Rechazada'
            self.reservas_rechazadas.append(reserva)
            self.guardar_reservas_pendientes()


    def obtener_reservas_aprobadas(self):
        return self.reservas_aprobadas

    def obtener_reservas_pendientes(self):
        # Obtener solo las reservas pendientes
        return self.reservas_pendientes

    def contar_reservas_aprobadas(self):
        return len(self.reservas_aprobadas)