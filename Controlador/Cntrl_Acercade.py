from PyQt6 import QtWidgets
from Modelo.Usuarios import ModeloUsuario
from Modelo.guardarusuario import Configuracion
from Vista.ventana_acercade import Ui_Form


class Controlador_acerca_de(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.modelo_usuario = ModeloUsuario()
        self.modelo_usuario.cargar_usuarios()
        self.ui.btn_regresar.clicked.connect(self.regresar)

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
