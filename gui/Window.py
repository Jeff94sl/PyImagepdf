from pathlib import Path
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from PDF.pdfimage import Convert
from gui.Lista import Lista


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyImgpdf")
        self.resize(400, 300)

        self.pdf = Convert()
        self.msg = QMessageBox()

        vl = QVBoxLayout()
        hl = QHBoxLayout()

        self.lista = Lista()
        agregar = QPushButton(self.tr('Aceptar'))
        agregar.clicked.connect(self.event_agregar)
        eliminar = QPushButton("Eliminar")
        eliminar.clicked.connect(self.event_eliminar)
        convertir = QPushButton("Convertir")
        convertir.clicked.connect(self.event_convertir)

        hl.addWidget(agregar)
        hl.addWidget(eliminar)
        hl.addWidget(convertir)

        vl.addWidget(self.lista)

        vl.addLayout(hl)

        self.setLayout(vl)

    def event_agregar(self):
        filename, _ = QFileDialog.getOpenFileName(self.parentWidget(), 'Agregar Imagen', f'{Path.home()}',
                                                  'Imagenes(*.jpeg *.jpg *.png)')
        if not filename:
            print('filename es vacio')
        else:
            self.lista.agregar(filename)
            print('filename no es vacio')


    def event_eliminar(self):
        if self.lista.modelo.rowCount() > 0:
            self.lista.eliminar()

    def event_convertir(self):
        if self.lista.modelo.rowCount() > 0:
            filename, _ = QFileDialog.getSaveFileName(self.parentWidget(), 'Guardar Pdf', f'{Path.home()}', 'Pdf(*.pdf)')
            self.pdf.imgtopdfautosize(filename, self.lista.lista)
            self.msg.setWindowTitle('Convertido')
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText('Convercion Completada!')
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
            self.lista.lista.clear()
            self.lista.modelo.setStringList(self.lista.lista)
        else:
            self.msg.setWindowTitle('Error')
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText('Agrege imagenes para poder convertir!')
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()