from collections import Counter

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Modelo.guardarusuario import Configuracion
from Vista.ventanaprincipal import Ui_MainWindow
from Modelo.Usuarios import ModeloUsuario
from Modelo.Reservas import ModeloReservas
from Modelo.Laboratorios import ModeloLaboratorio


class Controlador_Ventana_Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo_usuario = ModeloUsuario()
        self.modelo_usuario.cargar_usuarios()
        self.modelo_reservas = ModeloReservas()
        self.modelo_reservas.cargar_reservas_aprobadas()
        self.modelo_reservas.obtener_reservas_aprobadas()
        self.modelo_laboratorio=ModeloLaboratorio()
        user_role = Configuracion.usuario_actual
        self.set_menu_visibility(user_role)
        self.ui.actionGestionUsuarios.triggered.connect(self.crearusuario)
        self.ui.actionGestionLaboratorios.triggered.connect(self.crearlabs)
        self.ui.actionSolicitudes.triggered.connect(self.versolicitudes)
        self.ui.actionReservarLaboratorios.triggered.connect(self.reservarlab)
        self.ui.actionHorario_de_Laboratorio.triggered.connect(self.verlab)
        self.ui.actionReportesUsuarios.triggered.connect(self.reporte_laboratorios_usados)
        self.ui.actionReportesLaboratorios.triggered.connect(self.reporteslaboratorios)
        self.ui.actionInformacion.triggered.connect(self.acercade)
        self.ui.btn_regresar.clicked.connect(self.regresar)

    def set_menu_visibility(self, user_role):
        if user_role == "admin":
            self.ui.menuGestionar.menuAction().setVisible(True)
            for action in self.ui.menuGestionar.actions():
                action.setEnabled(True)
                action.setVisible(True)
        else:
            self.ui.menuGestionar.menuAction().setVisible(False)
            for action in self.ui.menuGestionar.actions():
                action.setEnabled(False)
                action.setVisible(False)
    def crearusuario(self):
        from Controlador.Cntrl_RegistarUsuarios import Controlador_RegistarUsuarios
        self.controladorcu = Controlador_RegistarUsuarios()
        self.controladorcu.show()
        self.close()

    def crearlabs(self):
        from Controlador.Cntrl_CrearLaboratorios import Controlador_crearlabs
        self.controladorcl=Controlador_crearlabs()
        self.controladorcl.show()
        self.close()

    def versolicitudes(self):
        try:
            from Controlador.Cntrl_Solicitudes import Controlador_Ver_Solicitudes
            self.controladorvs = Controlador_Ver_Solicitudes()
            self.controladorvs.show()
            self.close()
        except Exception as e:
            print(f"An exception occurred: {e}")

    def reservarlab(self):
        from Controlador.Cntrl_ReservarLaboratorio import Controlador_Reservar_Laboratorio
        self.controladorrl=Controlador_Reservar_Laboratorio()
        self.controladorrl.show()
        self.close()

    def verlab(self):
        from Controlador.Cntrl_VerLaboratorio import Controlador_Ver_Laboratorio
        self.controladorvl=Controlador_Ver_Laboratorio()
        self.controladorvl.show()
        self.close()

    def reporteslaboratorios(self):
        reservas_aprobadas = self.modelo_reservas.obtener_reservas_aprobadas()
        codigo_laboratorio, nombre_laboratorio = self.encontrar_elemento_mas_comun(reservas_aprobadas, lambda reserva: reserva['laboratorio'])

        if codigo_laboratorio is None:
            QMessageBox.information(self, "Reportes", "No hay reservas aprobadas para generar el reporte de laboratorios.")
            return
        QMessageBox.information(self, "Reportes", f"El laboratorio más reservado es:\nCódigo: {codigo_laboratorio}\nNombre: {nombre_laboratorio}")

    def reporte_laboratorios_usados(self):
        todos_laboratorios = self.modelo_laboratorio.obtener_todos_los_laboratorios()
        reservas_aprobadas = self.modelo_reservas.obtener_reservas_aprobadas()
        reservas_por_laboratorio = {}
        laboratorios_con_reserva = set()
        for reserva in reservas_aprobadas:
            laboratorio = reserva['laboratorio']
            reservas_por_laboratorio[laboratorio] = reservas_por_laboratorio.get(laboratorio, 0) + 1
            laboratorios_con_reserva.add(laboratorio)
        total_laboratorios = len(todos_laboratorios)
        total_laboratorios_reservados = len(laboratorios_con_reserva)
        mensaje = f"Total de laboratorios: {total_laboratorios}\n"
        mensaje += f"Total de laboratorios con al menos una reserva aprobada: {total_laboratorios_reservados}\n"
        for laboratorio, cantidad_reservas in reservas_por_laboratorio.items():
            mensaje += f"- Laboratorio {laboratorio}: {cantidad_reservas} reservas aprobadas\n"
        QMessageBox.information(self, "Reporte de Laboratorios Usados", mensaje)

    def encontrar_elemento_mas_comun(self, lista, key_func):
        elementos_mas_comunes = max(Counter(map(key_func, lista)).items(), key=lambda x: x[1], default=(None, 0))
        if elementos_mas_comunes[0] is not None:
            codigo_nombre = elementos_mas_comunes[0].split(' - ', 1)
            if len(codigo_nombre) == 2:
                return codigo_nombre[0], codigo_nombre[1]
        return None, None

    def acercade(self):
        from Controlador.Cntrl_Acercade import Controlador_acerca_de
        self.controladoracd=Controlador_acerca_de()
        self.controladoracd.setWindowTitle("Acerca De")
        self.controladoracd.show()
        self.close()

    def regresar(self):
        from Controlador.Cntrl_Login import Controlador_Login
        self.controladorl=Controlador_Login()
        self.controladorl.show()
        self.close()
