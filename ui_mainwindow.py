# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 471)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.actionRecorrido_en_Profundidad_Amplitud = QAction(MainWindow)
        self.actionRecorrido_en_Profundidad_Amplitud.setObjectName(u"actionRecorrido_en_Profundidad_Amplitud")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_agregar = QWidget()
        self.tab_agregar.setObjectName(u"tab_agregar")
        self.formLayout = QFormLayout(self.tab_agregar)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox_Particulas = QGroupBox(self.tab_agregar)
        self.groupBox_Particulas.setObjectName(u"groupBox_Particulas")
        self.gridLayout = QGridLayout(self.groupBox_Particulas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_id = QLineEdit(self.groupBox_Particulas)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.gridLayout.addWidget(self.lineEdit_id, 0, 1, 1, 1)

        self.spinBox_destinoY = QSpinBox(self.groupBox_Particulas)
        self.spinBox_destinoY.setObjectName(u"spinBox_destinoY")
        self.spinBox_destinoY.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_destinoY, 4, 1, 1, 1)

        self.label_origenX = QLabel(self.groupBox_Particulas)
        self.label_origenX.setObjectName(u"label_origenX")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.label_destinoY = QLabel(self.groupBox_Particulas)
        self.label_destinoY.setObjectName(u"label_destinoY")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.label_green = QLabel(self.groupBox_Particulas)
        self.label_green.setObjectName(u"label_green")

        self.gridLayout.addWidget(self.label_green, 8, 0, 1, 1)

        self.spinBox_origenX = QSpinBox(self.groupBox_Particulas)
        self.spinBox_origenX.setObjectName(u"spinBox_origenX")
        self.spinBox_origenX.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_origenX, 1, 1, 1, 1)

        self.pushButton_AgregarInicio = QPushButton(self.groupBox_Particulas)
        self.pushButton_AgregarInicio.setObjectName(u"pushButton_AgregarInicio")
        font = QFont()
        font.setPointSize(8)
        self.pushButton_AgregarInicio.setFont(font)

        self.gridLayout.addWidget(self.pushButton_AgregarInicio, 10, 0, 1, 2)

        self.spinBox_green = QSpinBox(self.groupBox_Particulas)
        self.spinBox_green.setObjectName(u"spinBox_green")
        self.spinBox_green.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_green, 8, 1, 1, 1)

        self.label_origenY = QLabel(self.groupBox_Particulas)
        self.label_origenY.setObjectName(u"label_origenY")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.spinBox_destinoX = QSpinBox(self.groupBox_Particulas)
        self.spinBox_destinoX.setObjectName(u"spinBox_destinoX")
        self.spinBox_destinoX.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_destinoX, 3, 1, 1, 1)

        self.spinBox_red = QSpinBox(self.groupBox_Particulas)
        self.spinBox_red.setObjectName(u"spinBox_red")
        self.spinBox_red.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_red, 7, 1, 1, 1)

        self.lineEdit_velocidad = QLineEdit(self.groupBox_Particulas)
        self.lineEdit_velocidad.setObjectName(u"lineEdit_velocidad")

        self.gridLayout.addWidget(self.lineEdit_velocidad, 5, 1, 1, 1)

        self.label_velocidad = QLabel(self.groupBox_Particulas)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.spinBox_blue = QSpinBox(self.groupBox_Particulas)
        self.spinBox_blue.setObjectName(u"spinBox_blue")
        self.spinBox_blue.setMaximum(255)
        self.spinBox_blue.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.spinBox_blue, 9, 1, 1, 1)

        self.label_blue = QLabel(self.groupBox_Particulas)
        self.label_blue.setObjectName(u"label_blue")

        self.gridLayout.addWidget(self.label_blue, 9, 0, 1, 1)

        self.label_id = QLabel(self.groupBox_Particulas)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.label_destinoX = QLabel(self.groupBox_Particulas)
        self.label_destinoX.setObjectName(u"label_destinoX")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.label_red = QLabel(self.groupBox_Particulas)
        self.label_red.setObjectName(u"label_red")

        self.gridLayout.addWidget(self.label_red, 7, 0, 1, 1)

        self.spinBox_origenY = QSpinBox(self.groupBox_Particulas)
        self.spinBox_origenY.setObjectName(u"spinBox_origenY")
        self.spinBox_origenY.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_origenY, 2, 1, 1, 1)

        self.label_color = QLabel(self.groupBox_Particulas)
        self.label_color.setObjectName(u"label_color")

        self.gridLayout.addWidget(self.label_color, 6, 0, 1, 1)

        self.pushButton_AgregarFinal = QPushButton(self.groupBox_Particulas)
        self.pushButton_AgregarFinal.setObjectName(u"pushButton_AgregarFinal")

        self.gridLayout.addWidget(self.pushButton_AgregarFinal, 11, 0, 1, 2)

        self.pushButton_Mostrar = QPushButton(self.groupBox_Particulas)
        self.pushButton_Mostrar.setObjectName(u"pushButton_Mostrar")

        self.gridLayout.addWidget(self.pushButton_Mostrar, 12, 0, 1, 2)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.groupBox_Particulas)

        self.salida_Particulas = QPlainTextEdit(self.tab_agregar)
        self.salida_Particulas.setObjectName(u"salida_Particulas")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.salida_Particulas)

        self.tabWidget.addTab(self.tab_agregar, "")
        self.tab_tabla = QWidget()
        self.tab_tabla.setObjectName(u"tab_tabla")
        self.gridLayout_2 = QGridLayout(self.tab_tabla)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table = QTableWidget(self.tab_tabla)
        self.table.setObjectName(u"table")

        self.gridLayout_2.addWidget(self.table, 0, 0, 1, 6)

        self.lineEdit_IDParticula = QLineEdit(self.tab_tabla)
        self.lineEdit_IDParticula.setObjectName(u"lineEdit_IDParticula")
        self.lineEdit_IDParticula.setEnabled(True)
        self.lineEdit_IDParticula.setReadOnly(False)

        self.gridLayout_2.addWidget(self.lineEdit_IDParticula, 1, 0, 1, 1)

        self.pushButton_OrdenarID = QPushButton(self.tab_tabla)
        self.pushButton_OrdenarID.setObjectName(u"pushButton_OrdenarID")

        self.gridLayout_2.addWidget(self.pushButton_OrdenarID, 1, 1, 1, 1)

        self.pushButton_OrdenarDistancia = QPushButton(self.tab_tabla)
        self.pushButton_OrdenarDistancia.setObjectName(u"pushButton_OrdenarDistancia")

        self.gridLayout_2.addWidget(self.pushButton_OrdenarDistancia, 1, 2, 1, 1)

        self.pushButton_OrdenarVelocidad = QPushButton(self.tab_tabla)
        self.pushButton_OrdenarVelocidad.setObjectName(u"pushButton_OrdenarVelocidad")

        self.gridLayout_2.addWidget(self.pushButton_OrdenarVelocidad, 1, 3, 1, 1)

        self.pushButton_Buscar = QPushButton(self.tab_tabla)
        self.pushButton_Buscar.setObjectName(u"pushButton_Buscar")

        self.gridLayout_2.addWidget(self.pushButton_Buscar, 1, 4, 1, 1)

        self.pushButton_mostrarTabla = QPushButton(self.tab_tabla)
        self.pushButton_mostrarTabla.setObjectName(u"pushButton_mostrarTabla")

        self.gridLayout_2.addWidget(self.pushButton_mostrarTabla, 1, 5, 1, 1)

        self.tabWidget.addTab(self.tab_tabla, "")
        self.tab_particulas = QWidget()
        self.tab_particulas.setObjectName(u"tab_particulas")
        self.gridLayout_4 = QGridLayout(self.tab_particulas)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphicsView = QGraphicsView(self.tab_particulas)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.pushButton_Dibujar = QPushButton(self.tab_particulas)
        self.pushButton_Dibujar.setObjectName(u"pushButton_Dibujar")

        self.gridLayout_4.addWidget(self.pushButton_Dibujar, 1, 0, 1, 1)

        self.pushButton_Limpiar = QPushButton(self.tab_particulas)
        self.pushButton_Limpiar.setObjectName(u"pushButton_Limpiar")

        self.gridLayout_4.addWidget(self.pushButton_Limpiar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_particulas, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1050, 21))
        self.menuArchivo = QMenu(self.menuBar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menuBar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuAlgoritmos = QMenu(self.menuBar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuVer.menuAction())
        self.menuBar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuVer.addAction(self.actionGrafo)
        self.menuAlgoritmos.addAction(self.actionRecorrido_en_Profundidad_Amplitud)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algoritmia", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecorrido_en_Profundidad_Amplitud.setText(QCoreApplication.translate("MainWindow", u"Recorrido en Profundidad/Amplitud", None))
        self.groupBox_Particulas.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen(x):", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino(Y)", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"green:", None))
        self.pushButton_AgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen(Y)", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"blue:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"iD:", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino(X)", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"red:", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.pushButton_AgregarFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar al Final", None))
        self.pushButton_Mostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_agregar), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.lineEdit_IDParticula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Part\u00edcula", None))
        self.pushButton_OrdenarID.setText(QCoreApplication.translate("MainWindow", u"Ordenar por ID", None))
        self.pushButton_OrdenarDistancia.setText(QCoreApplication.translate("MainWindow", u"Ordenar por distancia", None))
        self.pushButton_OrdenarVelocidad.setText(QCoreApplication.translate("MainWindow", u"Ordenar por velocidad", None))
        self.pushButton_Buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_mostrarTabla.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tabla), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.pushButton_Dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.pushButton_Limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_particulas), QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

