from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAction, qApp
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from PDF.pdfimage import Convert
from gui.Lista import Lista


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyImgpdf")
        # Context Menu
        # self.setContextMenuPolicy(Qt.ActionsContextMenu)
        #Actions Context Menu
        # english = QAction(self.tr('English'), self)
        # quitAction = QAction(self.tr("Quit"), self)
        # quitAction.triggered.connect(qApp.quit)

        # self.addAction(english)
        # self.addAction(quitAction)

        self.resize(400, 300)

        self.pdf = Convert()
        self.msg = QMessageBox()

        vl = QVBoxLayout()
        hl = QHBoxLayout()

        self.lista = Lista()
        agregar = QPushButton(self.tr('Agregar'))
        agregar.clicked.connect(self.event_agregar)
        eliminar = QPushButton(self.tr('Eliminar'))
        eliminar.clicked.connect(self.event_eliminar)
        convertir = QPushButton(self.tr('Convertir'))
        convertir.clicked.connect(self.event_convertir)

        hl.addWidget(agregar)
        hl.addWidget(eliminar)
        hl.addWidget(convertir)

        vl.addWidget(self.lista)

        vl.addLayout(hl)

        self.setLayout(vl)

    def event_agregar(self):
        filename, _ = QFileDialog.getOpenFileName(self.parentWidget(), self.tr('Agregar Imagen'), f'{Path.home()}',
                                                  self.tr('Imagenes(*.jpeg *.jpg *.png)'))
        if not filename:
            print(self.tr('filename es vacio'))
        else:
            self.lista.agregar(filename)


    def event_eliminar(self):
        if self.lista.modelo.rowCount() > 0:
            self.lista.eliminar()

    def event_convertir(self):
        if self.lista.modelo.rowCount() > 0:
            filename, _ = QFileDialog.getSaveFileName(self.parentWidget(), self.tr('Guardar Pdf'), f'{Path.home()}', 'Pdf(*.pdf)')
            self.pdf.imgtopdfautosize(filename, self.lista.lista)
            self.msg.setWindowTitle(self.tr('Exito'))
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText(self.tr('Finalizado con exito!'))
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
            self.lista.lista.clear()
            self.lista.modelo.setStringList(self.lista.lista)
        else:
            self.msg.setWindowTitle(self.tr('Error'))
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText(self.tr('Agrege imagenes para poder convertir!'))
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()