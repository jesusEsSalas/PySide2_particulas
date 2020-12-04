from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor
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
        self.ui.pushButton_Buscar.clicked.connect(self.click_buscar)
        self.ui.pushButton_mostrarTabla.clicked.connect(self.click_mostrarTabla)
        self.ui.pushButton_Dibujar.clicked.connect(self.dibujar)
        self.ui.pushButton_Limpiar.clicked.connect(self.limpiar)
        self.ui.pushButton_OrdenarID.clicked.connect(self.ordenarID)
        self.ui.pushButton_OrdenarDistancia.clicked.connect(self.ordenarDistancia)
        self.ui.pushButton_OrdenarVelocidad.clicked.connect(self.ordenarVelocidad)
        self.ui.actionGrafo.triggered.connect(self.action_MostrarGrafo)
        self.ui.actionRecorrido_en_Profundidad_Amplitud.triggered.connect(self.action_Busquedas)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

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

    @Slot()
    def click_mostrarTabla(self):
        self.ui.table.setColumnCount(10)
        headers = ["id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad", "red", "green", "blue", "distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers)

        self.ui.table.setRowCount(len(self.admin))
        row = 0

        for particula in self.admin:
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.table.setItem(row, 0, id_widget)
            self.ui.table.setItem(row, 1, origen_x_widget)
            self.ui.table.setItem(row, 2, origen_y_widget)
            self.ui.table.setItem(row, 3, destino_x_widget)
            self.ui.table.setItem(row, 4, destino_y_widget)
            self.ui.table.setItem(row, 5, velocidad_widget)
            self.ui.table.setItem(row, 6, red_widget)
            self.ui.table.setItem(row, 7, green_widget)
            self.ui.table.setItem(row, 8, blue_widget)
            self.ui.table.setItem(row, 9, distancia_widget)
            row += 1

    @Slot()
    def click_buscar(self):
        self.ui.table.setColumnCount(10)
        headers = ["id", "origen_x", "origen_y", "destino_x", "destino_y", "velocidad", "red", "green", "blue", "distancia"]
        self.ui.table.setHorizontalHeaderLabels(headers)
        id = self.ui.lineEdit_IDParticula.text()
        found = False
        for particula in self.admin:
            if id == particula.id:
                self.ui.table.clear()
                self.ui.table.setRowCount(1)
                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.table.setItem(0, 0, id_widget)
                self.ui.table.setItem(0, 1, origen_x_widget)
                self.ui.table.setItem(0, 2, origen_y_widget)
                self.ui.table.setItem(0, 3, destino_x_widget)
                self.ui.table.setItem(0, 4, destino_y_widget)
                self.ui.table.setItem(0, 5, velocidad_widget)
                self.ui.table.setItem(0, 6, red_widget)
                self.ui.table.setItem(0, 7, green_widget)
                self.ui.table.setItem(0, 8, blue_widget)
                self.ui.table.setItem(0, 9, distancia_widget)
                found = True
                return
        
        if not found:
            QMessageBox.warning(self, 'Atención', f'La particula con el id {id} no fue encontarda')
    
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.admin:
            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()
    
    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def ordenarID(self):
        self.admin.sort_by_id()
        QMessageBox.information(self, "Éxito", "Se ordenaron las Partículas por ID")

    @Slot()
    def ordenarDistancia(self):
        self.admin.sort_by_distancia()
        QMessageBox.information(self, "Éxito", "Se ordenaron las Partículas por distancia")
    
    @Slot()
    def ordenarVelocidad(self):
        self.admin.sort_by_velocidad()
        QMessageBox.information(self, "Éxito", "Se ordenaron las Partículas por velocidad")

    @Slot()
    def action_MostrarGrafo(self):
        self.ui.salida_Particulas.clear()
        grafo = self.admin.mostrarG()
        self.ui.salida_Particulas.insertPlainText(grafo)

    @Slot()
    def action_Busquedas(self):
        origen_x = self.ui.spinBox_origenX.value()
        origen_y = self.ui.spinBox_origenY.value()
        origen = (origen_x, origen_y)
        if self.admin.busqueda_profundidad(origen_x, origen_y) and self.admin.busqueda_Amplitud(origen_x, origen_y):
            print("Origen: ", origen)
            print("\nBusqueda de profundidad")
            self.admin.busqueda_profundidad(origen_x, origen_y)
            print("\nBusqueda de amplitud")
            self.admin.busqueda_Amplitud(origen_x, origen_y)
        else:
            QMessageBox.information(self, "Ojo", "No se pudieron leer los datos")