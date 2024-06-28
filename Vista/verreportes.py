import os

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 386)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 760, 390))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 220, 91))
        self.label_3.setText("")
        c_path = os.path.join(current_dir, "imagenes/descarga.png")
        self.label_3.setPixmap(QtGui.QPixmap(c_path))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(375, 60, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(290, 120, 371, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_regresar = QtWidgets.QPushButton(parent=Form)
        self.btn_regresar.setEnabled(True)
        self.btn_regresar.setGeometry(QtCore.QRect(650, 10, 81, 61))
        self.btn_regresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_regresar.setStyleSheet("border-radius:5px;\n"
                                        "background-color: rgb(1, 106, 127);\n"
                                        "")
        icon = QtGui.QIcon()
        d_path = os.path.join(current_dir, "imagenes/hacia-atras.png")
        icon.addPixmap(QtGui.QPixmap(d_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_regresar.setIcon(icon)
        self.btn_regresar.setCheckable(False)
        self.btn_regresar.setObjectName("btn_regresar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Reportes"))
        self.label_8.setText(_translate("Form", ""))
        self.btn_regresar.setText(_translate("Form", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
