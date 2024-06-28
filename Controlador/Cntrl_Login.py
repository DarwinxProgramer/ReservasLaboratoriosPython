from PyQt6.QtWidgets import QMessageBox
from Modelo.Usuarios import ModeloUsuario
from Modelo.guardarusuario import Configuracion
from Vista.login import Ui_Form
from PyQt6 import QtWidgets


class Controlador_Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.modelo_usuario = ModeloUsuario()
        self.modelo_usuario.cargar_usuarios()
        usuarios = self.modelo_usuario.obtener_todos_los_usuarios()
        print(usuarios)
        self.ui.btn_ingresar.clicked.connect(self.validar_ingreso)

    def abrir_ventana_principal(self):
        try:
            from Controlador.Cntrl_VentanaPrincipal import Controlador_Ventana_Principal
            usuarios = self.modelo_usuario.obtener_todos_los_usuarios()
            if usuarios:
                for usuario in usuarios:
                    if usuario["email"] == self.ui.txt_user.text() and usuario["contrasena"] == self.ui.txt_contrasena.text():
                        print("Ingreso exitoso como", usuario["rol"])
                        Configuracion.usuario_actual = usuario["rol"]
                        self.controladorvp = Controlador_Ventana_Principal()
                        self.controladorvp.show()
                        self.close()
                        return
                print("Error: No se encontró un usuario con las credenciales proporcionadas.")
            else:
                print("Error: No hay usuarios registrados.")
        except Exception as e:
            print("Error al abrir la ventana principal:", str(e))

    def validar_ingreso(self):
        email = self.ui.txt_user.text()
        contrasena = self.ui.txt_contrasena.text()

        if not email or not contrasena:
            print("Error: Credenciales vacías")
            QMessageBox.critical(self, "Error", "Por favor, ingrese correo y contraseña")
            return

        print(f"Intentando ingresar con email: {email}, contraseña: {contrasena}")

        usuario = self.modelo_usuario.obtener_usuario_por_credenciales(email, contrasena)
        if usuario is not None:
            print("Ingreso exitoso como", usuario["rol"])
            self.abrir_ventana_principal()
        else:
            print("Error: Credenciales incorrectas")
            QMessageBox.critical(self, "Error", "Credenciales incorrectas")
