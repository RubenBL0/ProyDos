# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(595, 265)
        self.btnBoxSalir = QtWidgets.QDialogButtonBox(Dialog)
        self.btnBoxSalir.setGeometry(QtCore.QRect(140, 200, 341, 32))
        self.btnBoxSalir.setOrientation(QtCore.Qt.Horizontal)
        self.btnBoxSalir.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxSalir.setCenterButtons(True)
        self.btnBoxSalir.setObjectName("btnBoxSalir")
        self.lblMensaje = QtWidgets.QLabel(Dialog)
        self.lblMensaje.setGeometry(QtCore.QRect(240, 70, 201, 81))
        self.lblMensaje.setObjectName("lblMensaje")
        self.lblIcono = QtWidgets.QLabel(Dialog)
        self.lblIcono.setGeometry(QtCore.QRect(80, 60, 101, 101))
        self.lblIcono.setText("")
        self.lblIcono.setPixmap(QtGui.QPixmap(":/newPrefix/iconoaviso.png"))
        self.lblIcono.setScaledContents(True)
        self.lblIcono.setObjectName("lblIcono")

        self.retranslateUi(Dialog)
        self.btnBoxSalir.accepted.connect(Dialog.accept)
        self.btnBoxSalir.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aviso"))
        self.lblMensaje.setText(_translate("Dialog", "¿Seguro que desea salir de la aplicación?"))
import warning_rc
