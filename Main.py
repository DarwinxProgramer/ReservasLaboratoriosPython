from PyQt6 import QtWidgets
from Controlador.Cntrl_Login import Controlador_Login
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    print("Iniciando el programa")
    controlador_login = Controlador_Login()
    controlador_login.setWindowTitle("Login")
    controlador_login.show()
    sys.exit(app.exec())
