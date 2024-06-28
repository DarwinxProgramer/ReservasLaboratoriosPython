from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Modelo.guardarusuario import Configuracion
from Vista.registrarusuario import Ui_Form
from Modelo.Usuarios import ModeloUsuario


class Controlador_RegistarUsuarios(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.modelo_usuario = ModeloUsuario()
        self.ui.btn_registrar.clicked.connect(self.registrar_usuario)
        self.ui.btn_modificar.clicked.connect(self.modificar_usuario)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_usuario)
        self.ui.btn_buscar.clicked.connect(self.buscar_usuario)
        self.ui.btn_cancelar.clicked.connect(self.limpiar_campos)
        self.ui.btn_regresar.clicked.connect(self.regresar)

    def registrar_usuario(self):
        id = self.ui.txt_id.text()
        nombre = self.ui.txt_nombre.text()
        apellido = self.ui.txt_apellido.text()
        rol = self.ui.comboBox.currentText()
        email = self.ui.txt_email.text()
        contrasena = self.ui.txt_contrasena.text()

        if self.validar_campos(id, nombre, apellido, email, contrasena):
            self.modelo_usuario.crear_usuario(id, nombre, apellido, rol, email, contrasena)
            self.modelo_usuario.guardar_usuarios()
            QMessageBox.information(self, "Éxito", "Usuario creado correctamente.")
            print("Usuarios cargados:", self.modelo_usuario.obtener_todos_los_usuarios())
            self.limpiar_campos()
        else:
            QMessageBox.critical(self, "Error", "Datos incorrectos")

    def validar_campos(self, id, nombre, apellido, email, contrasena):
        if id.strip() or nombre.strip() or apellido.strip() or email.strip() or contrasena.strip():
            if nombre.isalpha() or apellido.isalpha():
                if email.endswith("@ucuenca.edu.ec"):
                    if (lambda id: sum([int(id[i]) if i % 2 != 0 else int(id[i]) * 2 if int(id[i]) * 2 < 9 else int(id[i]) * 2 - 9 for i in range(10)]) % 10 == 0)(id):
                        return True
        return False

    def limpiar_campos(self):
        self.ui.txt_id.clear()
        self.ui.txt_nombre.clear()
        self.ui.txt_apellido.clear()
        self.ui.txt_email.clear()
        self.ui.txt_contrasena.clear()

    def buscar_usuario(self):
        id = self.ui.txt_idbuscar.text()
        usuario = self.modelo_usuario.buscar_usuario_por_id(id)
        if usuario:
            self.ui.txt_id.setText(usuario["id"])
            self.ui.txt_nombre.setText(usuario["nombre"])
            self.ui.txt_apellido.setText(usuario["apellido"])
            self.ui.comboBox.setCurrentText(usuario["rol"])
            self.ui.txt_email.setText(usuario["email"])
            self.ui.txt_contrasena.setText(usuario["contrasena"])
        else:
            QMessageBox.warning(self, "Usuario no encontrado", "No se encontró un usuario con el ID proporcionado.")

    def eliminar_usuario(self):
        id = self.ui.txt_id.text()
        if self.modelo_usuario.eliminar_usuario_por_id(id):
            QMessageBox.information(self, "Usuario eliminado", "Usuario eliminado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el usuario. Verifica el ID proporcionado.")

    def modificar_usuario(self):
        codigo = self.ui.txt_id.text()
        nuevos_datos = {
            "nombre": self.ui.txt_nombre.text(),
            "apellido": self.ui.txt_apellido.text(),
            "rol": self.ui.comboBox.currentText(),
            "email": self.ui.txt_email.text(),
            "contrasena": self.ui.txt_contrasena.text()
        }
        if self.modelo_usuario.modificar_usuario(codigo, nuevos_datos):
            QMessageBox.information(self, "Usuario modificado", "Usuario modificado exitosamente.")
            self.limpiar_campos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo modificar el usuario. Verifica el ID proporcionado.")

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
