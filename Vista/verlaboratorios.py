# Form implementation generated from reading ui file 'verlaboratorios.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(955, 586)
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 960, 581))
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
        self.btn_regresar.setGeometry(QtCore.QRect(850, 10, 81, 61))
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
        self.cbox_laboratorios = QtWidgets.QComboBox(parent=Form)
        self.cbox_laboratorios.setGeometry(QtCore.QRect(290, 150, 371, 22))
        self.cbox_laboratorios.setObjectName("cbox_laboratorios")
        self.btn_ver = QtWidgets.QPushButton(parent=Form)
        self.btn_ver.setGeometry(QtCore.QRect(700, 150, 92, 28))
        self.btn_ap = QtWidgets.QPushButton(parent=Form)
        self.btn_ap.setGeometry(QtCore.QRect(700, 200, 92, 28))
        self.btn_re = QtWidgets.QPushButton(parent=Form)
        self.btn_re.setGeometry(QtCore.QRect(700, 250, 92, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_ver.setFont(font)
        self.btn_ver.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_ver.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"border-radius:5px;")
        self.btn_ver.setObjectName("btn_ver")
        self.btn_ver.setFont(font)
        self.btn_ap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_ap.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                   "border-radius:5px;")
        self.btn_ap.setObjectName("btn_ap")
        self.btn_re.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btn_re.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                  "border-radius:5px;")
        self.btn_re.setObjectName("btn_ap")
        self.table_laboratorios = QtWidgets.QTableWidget(parent=Form)
        self.table_laboratorios.setGeometry(QtCore.QRect(240, 200, 440, 370))
        self.table_laboratorios.setObjectName("table_laboratorios")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(0, 110, 100, 481))
        self.label_4.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Ver Laboratorios"))
        self.label_8.setText(_translate("Form", "Selecione el laboratorio para ver su horario:"))
        self.btn_regresar.setText(_translate("Form", "Regresar"))
        self.btn_ver.setText(_translate("Form", "Ver"))
        self.btn_ap.setText(_translate("Form", "Aprobar"))
        self.btn_re.setText(_translate("Form", "Rechazar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())