# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VenPrincipal(object):
    def setupUi(self, VenPrincipal):
        VenPrincipal.setObjectName("VenPrincipal")
        VenPrincipal.resize(800, 596)
        self.centralwidget = QtWidgets.QWidget(VenPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblSaludo = QtWidgets.QLabel(self.centralwidget)
        self.lblSaludo.setEnabled(True)
        self.lblSaludo.setGeometry(QtCore.QRect(270, 270, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblSaludo.setFont(font)
        self.lblSaludo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSaludo.setObjectName("lblSaludo")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(360, 400, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        VenPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VenPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        VenPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VenPrincipal)
        self.statusbar.setObjectName("statusbar")
        VenPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(VenPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(VenPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VenPrincipal)

    def retranslateUi(self, VenPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VenPrincipal.setWindowTitle(_translate("VenPrincipal", "Proyecto Grupo B"))
        self.lblSaludo.setText(_translate("VenPrincipal", "HOLA MUNDO"))
        self.btnAceptar.setText(_translate("VenPrincipal", "Aceptar"))
        self.menuArchivo.setTitle(_translate("VenPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("VenPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("VenPrincipal", "Ctrl+S"))
