from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QInputDialog
from Modelo.Reservas import ModeloReservas
from Modelo.Laboratorios import ModeloLaboratorio
from Modelo.Usuarios import ModeloUsuario
from Modelo.guardarusuario import Configuracion
from Vista.reservarlaboratorios import Ui_Form
from datetime import datetime


class Controlador_Reservar_Laboratorio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.modelo_laboratorios = ModeloLaboratorio()  # Agregar los paréntesis para crear una instancia del modelo
        self.modelo_reservas = ModeloReservas()
        self.modelo_usuario = ModeloUsuario()
        self.modelo_usuario.cargar_usuarios()
        laboratorios_disponibles = [f"{lab['codigo']} - {lab['nombre']} " for lab in self.modelo_laboratorios.obtener_todos_los_laboratorios()]
        self.ui.cbox_laboratorios.addItems(laboratorios_disponibles)
        self.ui.btn_regresar.clicked.connect(self.regresar)
        self.ui.btn_reservar.clicked.connect(self.reservar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)
        print(self.modelo_reservas.obtener_reservas_pendientes())

    def reservar(self):
        rol, ok = QInputDialog.getText(self, "Ingresar Rol", "Ingrese su rol:")
        if not ok:
            return
        laboratorio_seleccionado = self.ui.cbox_laboratorios.currentText()
        if not laboratorio_seleccionado:
            QMessageBox.critical(self, "Error", "Por favor, seleccione un laboratorio.")
            return
        fecha_seleccionada = self.ui.calendarWidget.selectedDate().toString(Qt.DateFormat.ISODate)
        hora_seleccionada = self.ui.timeEdit_hora.time().toString(Qt.DateFormat.ISODate)
        if not fecha_seleccionada or not hora_seleccionada:
            QMessageBox.critical(self, "Error", "Por favor, seleccione una fecha y hora válidas.")
            return
        fecha_objeto = datetime.strptime(fecha_seleccionada, "%Y-%m-%d").date()
        fecha_limite = datetime(2023, 12, 25).date()
        if fecha_objeto <= fecha_limite:
            QMessageBox.critical(self, "Error", "La fecha debe ser posterior al 25 de diciembre de 2023.")
            return

        # Convertir la hora seleccionada a objeto de tiempo de Python
        hora_objeto = datetime.strptime(hora_seleccionada, "%H:%M:%S").time()

        # Validar que la hora esté en el rango de 7 a 19
        hora_inicio = datetime.strptime("07:00:00", "%H:%M:%S").time()
        hora_fin = datetime.strptime("19:00:00", "%H:%M:%S").time()

        if not hora_inicio <= hora_objeto <= hora_fin:
            QMessageBox.critical(self, "Error", "La hora debe estar en el rango de 7:00 a 19:00.")
            return
        self.modelo_reservas.realizar_reserva(laboratorio_seleccionado, fecha_seleccionada, hora_seleccionada, rol)
        QMessageBox.information(self, "Éxito", "Reserva realizada correctamente.")
        self.modelo_reservas.guardar_reservas_pendientes()
        print("Reserva: ", self.modelo_reservas.obtener_reservas_pendientes())

    def cancelar(self):
        self.ui.cbox_laboratorios.setCurrentIndex(-1)
        self.ui.calendarWidget.clearMask()
        self.ui.timeEdit_hora.clear()

    def regresar(self):
        try:
            print("Regresando a la ventana principal")
            from Controlador.Cntrl_VentanaPrincipal import Controlador_Ventana_Principal
            user_role = Configuracion.usuario_actual
            if hasattr(self, 'controladorvp') and isinstance(self.controladorvp, Controlador_Ventana_Principal):
                self.controladorvp.set_menu_visibility(user_role)
                self.controladorvp.show()
            else:
                self.controladorvp = Controlador_Ventana_Principal()
                self.controladorvp.set_menu_visibility(user_role)
                self.controladorvp.show()
            self.close()
        except Exception as e:
            print(f"Error al regresar: {e}")
