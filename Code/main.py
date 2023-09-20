import sys
import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase, QFont

from MainWindow.ui import Ui_MainWindow

from imageMenu import ImageMenu

class ProgramUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(ProgramUI, self).__init__()

        # Ui initialization
        self.scraper = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Fonts
        self.fontDB = QFontDatabase()
        self.fontDB.addApplicationFont(":/Fonts/Fonts/Montserrat-ExtraBold.ttf")
        self.fontDB.addApplicationFont(":/Fonts/Fonts/Montserrat-SemiBold.ttf")

        # Initialization
        self.setWindowTitle("SGraphy")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(":/Icons/Icons/sgraphy.png"))

        self.ui.imageDropbox.setAcceptDrops(True)

        # Intializing components
        ImageMenu(self).initialize()

        # Intializing explorer
        self.explorerInitialize()

    def explorerInitialize(self):
        self.ui.imagesButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.musicButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.docsButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.textButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.otherButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))




# Program start
app = QtWidgets.QApplication([])
a = ProgramUI()
a.show()

# Program exit
sys.exit(app.exec())