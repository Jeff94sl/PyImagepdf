from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction

class Menu(QMenuBar):
    def __init__(self):
        super(Menu, self).__init__()
        archivo = QMenu("&Archivo",self)
        abrir = QAction("A&brir",self)
        archivo.addAction(abrir)
        self.addMenu(archivo)