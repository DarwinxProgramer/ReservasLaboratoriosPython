from Modelo.Usuarios import ModeloUsuario
from Modelo.guardarusuario import Configuracion
from Vista.crearlaboratorios import Ui_Form
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Modelo.Laboratorios import ModeloLaboratorio


class Controlador_crearlabs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.modelo_laboratorio = ModeloLaboratorio()
        self.modelo_usuario = ModeloUsuario()
        self.modelo_usuario.cargar_usuarios()
        self.ui.btn_regresar.clicked.connect(self.regresar)
        self.ui.btn_registrar.clicked.connect(self.crear_laboratorio)
        self.ui.btn_cancelar.clicked.connect(self.limpiar_campos)
        self.ui.btn_buscar.clicked.connect(self.buscar_laboratorio)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_laboratorio)
        self.ui.btn_modificar.clicked.connect(self.modificar_laboratorio)
        print(self.modelo_laboratorio.obtener_todos_los_laboratorios())

    def crear_laboratorio(self):
        codigo = self.ui.txt_codigo.text()
        nombre = self.ui.txt_nombrelab.text()
        capacidad = self.ui.txt_id.text()

        if not codigo or not nombre or not capacidad:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
            return
        try:
            capacidad = int(capacidad)
        except ValueError:
            QMessageBox.critical(self, "Error", "La capacidad debe ser un número entero.")
            return

        softwares = []
        if self.ui.chbox_IntellijIIDEA.isChecked():
            softwares.append("Intellij IDEA")
        if self.ui.chbox_Julia.isChecked():
            softwares.append("Julia")
        if self.ui.chbox_dvc.isChecked():
            softwares.append("Devc++")
        if self.ui.chbox_netBeans.isChecked():
            softwares.append("NetBeans")
        if self.ui.chbox_otro.isChecked():
            otro_software = self.ui.txt_otro.text().strip()
            if not otro_software:
                QMessageBox.critical(self, "Error", "Por favor, ingrese el nombre del otro software.")
                return
            softwares.append(otro_software)
        try:
            self.modelo_laboratorio.crear_laboratorio(
                codigo,
                nombre,
                capacidad,
                softwares
            )
            QMessageBox.information(self, "Éxito", "Laboratorio creado correctamente.")
            self.modelo_laboratorio.guardar_laboratorios()
            print("Laboratorios: ", self.modelo_laboratorio.obtener_todos_los_laboratorios())
            self.limpiar_campos()
            self.desmarcar_softwares()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear el laboratorio: {e}")

    def limpiar_campos(self):
        self.ui.txt_codigo.clear()
        self.ui.txt_nombrelab.clear()
        self.ui.txt_id.clear()
        self.ui.txt_otro.clear()
        self.desmarcar_softwares()

    def desmarcar_softwares(self):
        self.ui.chbox_IntellijIIDEA.setChecked(False)
        self.ui.chbox_Julia.setChecked(False)
        self.ui.chbox_dvc.setChecked(False)
        self.ui.chbox_netBeans.setChecked(False)
        self.ui.chbox_otro.setChecked(False)

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

    def buscar_laboratorio(self):
        codigo = self.ui.txt_idbuscar.text()
        laboratorio = self.modelo_laboratorio.buscar_laboratorio_por_codigo(codigo)
        if laboratorio:
            self.ui.txt_codigo.setText(laboratorio["codigo"])
            self.ui.txt_nombrelab.setText(laboratorio["nombre"])
            self.ui.txt_id.setText(str(laboratorio["capacidad"]))
            self.marcar_softwares(laboratorio["softwares"])
        else:
            QMessageBox.warning(self, "Laboratorio no encontrado ", "No se encontró un laboratorio con el código dado.")

    def marcar_softwares(self, softwares):
        self.ui.chbox_IntellijIIDEA.setChecked(False)
        self.ui.chbox_Julia.setChecked(False)
        self.ui.chbox_dvc.setChecked(False)
        self.ui.chbox_netBeans.setChecked(False)
        self.ui.chbox_otro.setChecked(False)
        for software in softwares:
            if software == "Intellij IDEA":
                self.ui.chbox_IntellijIIDEA.setChecked(True)
            elif software == "Julia":
                self.ui.chbox_Julia.setChecked(True)
            elif software == "Devc++":
                self.ui.chbox_dvc.setChecked(True)
            elif software == "NetBeans":
                self.ui.chbox_netBeans.setChecked(True)
            else:
                self.ui.chbox_otro.setChecked(True)
                self.ui.txt_otro.setText(software)

    def eliminar_laboratorio(self):
        codigo = self.ui.txt_idbuscar.text()
        if self.modelo_laboratorio.eliminar_laboratorio_por_codigo(codigo):
            QMessageBox.information(self, "Laboratorio eliminado", "Laboratorio eliminado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el laboratorio. Verifica el código proporcionado.")

    def modificar_laboratorio(self):
        codigo = self.ui.txt_idbuscar.text()
        print(f"Código a modificar: {codigo}")
        if not self.modelo_laboratorio.buscar_laboratorio_por_codigo(codigo):
            QMessageBox.warning(self, "Error", "No se encontró el laboratorio. Verifica el código proporcionado.")
            return
        nuevos_datos = {
            "codigo": self.ui.txt_codigo.text(),
            "nombre": self.ui.txt_nombrelab.text(),
            "capacidad": int(self.ui.txt_id.text()),
            "softwares": self.obtener_softwares_seleccionados()
        }
        if self.modelo_laboratorio.modificar_laboratorio(codigo, nuevos_datos):
            QMessageBox.information(self, "Éxito", "Laboratorio modificado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo modificar el laboratorio. Verifica el código proporcionado.")

    def obtener_softwares_seleccionados(self):
        softwares_seleccionados = []

        if self.ui.chbox_IntellijIIDEA.isChecked():
            softwares_seleccionados.append("Intellij IDEA")
        if self.ui.chbox_Julia.isChecked():
            softwares_seleccionados.append("Julia")
        if self.ui.chbox_dvc.isChecked():
            softwares_seleccionados.append("Devc++")
        if self.ui.chbox_netBeans.isChecked():
            softwares_seleccionados.append("NetBeans")
        if self.ui.chbox_otro.isChecked():
            otro_software = self.ui.txt_otro.text().strip()
            if otro_software:
                softwares_seleccionados.append(otro_software)

        return softwares_seleccionados
