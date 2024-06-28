from PyQt6.QtWidgets import QMainWindow

from Modelo.Usuarios import ModeloUsuario
from Modelo.guardarusuario import Configuracion
from Vista.verlaboratorios import Ui_Form
from Modelo.Reservas import ModeloReservas
from Modelo.Laboratorios import ModeloLaboratorio
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox


class Controlador_Ver_Laboratorio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.modelo_reservas = ModeloReservas()
        self.modelo_laboratorios = ModeloLaboratorio()
        self.modelo_reservas.cargar_reservas_aprobadas()
        self.modelo_reservas.obtener_reservas_aprobadas()
        self.modelo_usuario = ModeloUsuario()
        self.modelo_usuario.cargar_usuarios()
        laboratorios_disponibles = [f"{lab['codigo']} - {lab['nombre']} " for lab in self.modelo_laboratorios.obtener_todos_los_laboratorios()]
        self.ui.cbox_laboratorios.addItems(laboratorios_disponibles)
        self.ui.btn_ver.clicked.connect(self.llenartabla)
        self.ui.btn_regresar.clicked.connect(self.regresar)
        self.ui.table_laboratorios.hide()
        self.ui.btn_ap.hide()
        self.ui.btn_re.hide()

    def llenartabla(self):
        laboratorio_seleccionado_texto = self.ui.cbox_laboratorios.currentText()
        codigo_laboratorio_seleccionado = laboratorio_seleccionado_texto.split('-')[0].strip()
        reservas_aprobadas = self.modelo_reservas.obtener_reservas_aprobadas()
        reservas_filtradas = [
            reserva for reserva in reservas_aprobadas
            if reserva.get('laboratorio', '').startswith(codigo_laboratorio_seleccionado)
        ]
        if not reservas_filtradas:
            QMessageBox.information(self, "Información", f"No hay reservas aprobadas para el laboratorio {codigo_laboratorio_seleccionado}.")
            return
        self.ui.table_laboratorios.setRowCount(0)
        self.ui.table_laboratorios.setColumnCount(5)
        self.ui.table_laboratorios.setHorizontalHeaderLabels(['Laboratorio', 'Fecha', 'Hora', 'Rol', 'Reserva'])
        for reserva in reservas_filtradas:
            rowPosition = self.ui.table_laboratorios.rowCount()
            self.ui.table_laboratorios.insertRow(rowPosition)
            self.ui.table_laboratorios.setItem(rowPosition, 0, QTableWidgetItem(reserva.get('laboratorio', '')))
            self.ui.table_laboratorios.setItem(rowPosition, 1, QTableWidgetItem(reserva.get('fecha', '')))
            self.ui.table_laboratorios.setItem(rowPosition, 2, QTableWidgetItem(reserva.get('hora', '')))
            self.ui.table_laboratorios.setItem(rowPosition, 3, QTableWidgetItem(reserva.get('rol', '')))
            estado = reserva.get('estado', 'Aprobado')
            self.ui.table_laboratorios.setItem(rowPosition, 4, QTableWidgetItem(estado))
        self.ui.table_laboratorios.resizeColumnsToContents()
        self.ui.table_laboratorios.show()

    def regresar(self):
        try:
            print("Regresando a la ventana principal")
            from Controlador.Cntrl_VentanaPrincipal import Controlador_Ventana_Principal
            user_role = Configuracion.usuario_actual
            if hasattr(self, 'controladorvp') and isinstance(self.controladorvp, Controlador_Ventana_Principal):
                # Actualizar el rol del usuario en la instancia existente y mostrarla
                self.controladorvp.set_menu_visibility(user_role)
                self.controladorvp.show()
            else:
                self.controladorvp = Controlador_Ventana_Principal()
                self.controladorvp.set_menu_visibility(user_role)
                self.controladorvp.show()
            self.close()
        except Exception as e:
            print(f"Error al regresar: {e}")
