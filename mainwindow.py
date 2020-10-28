from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas import Particula
from admin_particulas import Administradora

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.admin = Administradora()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Mostrar.clicked.connect(self.click_mostrar)
        self.ui.pushButton_AgregarInicio.clicked.connect(self.click_agregarInicio)
        self.ui.pushButton_AgregarFinal.clicked.connect(self.click_agregarFinal)
        self.ui.actionAbrir.triggered.connect(self.action_abrirArchivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardarArchivo)

    @Slot()
    def click_mostrar(self):
        self.ui.salida_Particulas.clear()
        self.ui.salida_Particulas.insertPlainText(str(self.admin))
    
    @Slot()
    def click_agregarInicio(self):
        id = self.ui.lineEdit_id.text()
        origen_x = self.ui.spinBox_origenX.value()
        origen_y = self.ui.spinBox_origenY.value()
        destino_x = self.ui.spinBox_destinoX.value()
        destino_y = self.ui.spinBox_destinoY.value()
        velocidad = self.ui.lineEdit_velocidad.text()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregar_inicio(particula)

    @Slot()
    def click_agregarFinal(self):
        id = self.ui.lineEdit_id.text()
        origen_x = self.ui.spinBox_origenX.value()
        origen_y = self.ui.spinBox_origenY.value()
        destino_x = self.ui.spinBox_destinoX.value()
        destino_y = self.ui.spinBox_destinoY.value()
        velocidad = self.ui.lineEdit_velocidad.text()
        red = self.ui.spinBox_red.value()
        green = self.ui.spinBox_green.value()
        blue = self.ui.spinBox_blue.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.admin.agregar_final(particula)

    @Slot()
    def action_guardarArchivo(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'JSON (*.json)')[0]
        if self.admin.guardar(ubicacion):
            QMessageBox.information(self, "Éxito", "Se pudo crear el archivo" + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "No se pudo crear el archivo" + ubicacion)

    @Slot()
    def action_abrirArchivo(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir Archivo', '.', 'JSON(*.json)')[0]
        if self.admin.abrir(ubicacion):
            QMessageBox.information(self, "Éxito", "Se abrió el archivo" + ubicacion)
        else:
            QMessageBox.critical(self, "Error", "Error al abrir el archivo" + ubicacion)
