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
        VenPrincipal.resize(1040, 800)
        self.centralwidget = QtWidgets.QWidget(VenPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(430, 490, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(360, 60, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Himalaya")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAutoFillBackground(False)
        self.lblTitulo.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0.431818, y1:0, x2:0.494, y2:1, stop:0 rgba(49, 3, 188, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitulo.setWordWrap(False)
        self.lblTitulo.setObjectName("lblTitulo")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(100, 190, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.lblApelidos = QtWidgets.QLabel(self.centralwidget)
        self.lblApelidos.setGeometry(QtCore.QRect(100, 243, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblApelidos.setFont(font)
        self.lblApelidos.setObjectName("lblApelidos")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(600, 233, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(550, 490, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        self.entDNI = QtWidgets.QLineEdit(self.centralwidget)
        self.entDNI.setGeometry(QtCore.QRect(210, 190, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entDNI.setFont(font)
        self.entDNI.setMaxLength(9)
        self.entDNI.setObjectName("entDNI")
        self.entApelidos = QtWidgets.QLineEdit(self.centralwidget)
        self.entApelidos.setGeometry(QtCore.QRect(210, 250, 351, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entApelidos.setFont(font)
        self.entApelidos.setMaxLength(50)
        self.entApelidos.setObjectName("entApelidos")
        self.entNome = QtWidgets.QLineEdit(self.centralwidget)
        self.entNome.setGeometry(QtCore.QRect(670, 250, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entNome.setFont(font)
        self.entNome.setMaxLength(50)
        self.entNome.setObjectName("entNome")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 140, 911, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 470, 911, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 300, 271, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lytSexo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.lytSexo.setContentsMargins(0, 0, 0, 0)
        self.lytSexo.setObjectName("lytSexo")
        self.rbtFem = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rbtFem.setFont(font)
        self.rbtFem.setObjectName("rbtFem")
        self.lytSexo.addWidget(self.rbtFem)
        self.rbtMasc = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtMasc.setObjectName("rbtMasc")
        self.lytSexo.addWidget(self.rbtMasc)
        self.lblSexo = QtWidgets.QLabel(self.centralwidget)
        self.lblSexo.setGeometry(QtCore.QRect(100, 323, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.lblPago = QtWidgets.QLabel(self.centralwidget)
        self.lblPago.setGeometry(QtCore.QRect(510, 320, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(670, 300, 361, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkEfect = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkEfect.setObjectName("chkEfect")
        self.horizontalLayout.addWidget(self.chkEfect)
        self.chkTarj = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkTarj.setObjectName("chkTarj")
        self.horizontalLayout.addWidget(self.chkTarj)
        self.chkTrans = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkTrans.setObjectName("chkTrans")
        self.horizontalLayout.addWidget(self.chkTrans)
        self.lblValido = QtWidgets.QLabel(self.centralwidget)
        self.lblValido.setGeometry(QtCore.QRect(370, 180, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblValido.setFont(font)
        self.lblValido.setText("")
        self.lblValido.setObjectName("lblValido")
        self.lblPrueba = QtWidgets.QLabel(self.centralwidget)
        self.lblPrueba.setGeometry(QtCore.QRect(230, 400, 161, 31))
        self.lblPrueba.setText("")
        self.lblPrueba.setObjectName("lblPrueba")
        VenPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VenPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 21))
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
        self.btnAceptar.setText(_translate("VenPrincipal", "Aceptar"))
        self.lblTitulo.setText(_translate("VenPrincipal", "XESTIÓN CLIENTES"))
        self.lblDNI.setText(_translate("VenPrincipal", "DNI:"))
        self.lblApelidos.setText(_translate("VenPrincipal", "Apelidos: "))
        self.lblNome.setText(_translate("VenPrincipal", "Nome: "))
        self.btnSalir.setText(_translate("VenPrincipal", "Salir"))
        self.rbtFem.setText(_translate("VenPrincipal", "Femenino"))
        self.rbtMasc.setText(_translate("VenPrincipal", "Masculino"))
        self.lblSexo.setText(_translate("VenPrincipal", "Sexo:"))
        self.lblPago.setText(_translate("VenPrincipal", "Métodos de Pago:"))
        self.chkEfect.setText(_translate("VenPrincipal", "Efectivo"))
        self.chkTarj.setText(_translate("VenPrincipal", "Tarjeta"))
        self.chkTrans.setText(_translate("VenPrincipal", "Transferencia"))
        self.menuArchivo.setTitle(_translate("VenPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("VenPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("VenPrincipal", "Ctrl+S"))
