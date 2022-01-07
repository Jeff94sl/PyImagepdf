import sys
from PyQt5.QtCore import QLocale,QTranslator,QLibraryInfo
from PyQt5.QtWidgets import QApplication
from gui.Window import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)

    traductor = QTranslator()
    traductor.load("qtbase_"+ QLocale.system().name(),
                   QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(traductor)

    win = Window()
    win.show()
    sys.exit(app.exec_())