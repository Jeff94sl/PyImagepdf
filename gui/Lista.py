from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QListView


class Lista(QListView):
    def __init__(self):
        super(Lista, self).__init__()
        self.lista = []
        self.modelo = QStringListModel()
        self.modelo.setStringList(self.lista)
        self.setModel(self.modelo)

    def agregar(self, item):
        self.lista.append(item)
        self.modelo.setStringList(self.lista)

    def eliminar(self):
        self.modelo.removeRow(self.modelo.rowCount() - 1)
        del self.lista[- 1]
        print("Modelo: ", self.modelo.rowCount())
        print(self.listacount())

    def listacount(self):
        count = 0
        for _ in self.lista:
            count += 1
        return count
