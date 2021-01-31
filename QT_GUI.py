from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *#QApplication, QWidget, QVBoxLayout, QGridLayout, QSizeGrip, QPushButton, QLineEdit, QStyleFactory, QMainWindow
import sys


class Window(QMainWindow):
    def init(self):
        self.title = "PyQt5 GUI"

        # Window properties
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("icon.png"))

        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        # self.setStyleSheet('background-color: #28262C')

        # Flags
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0.7)
        painter.setBrush(Qt.black)
        painter.setPen(QPen(Qt.black))
        painter.drawRect(self.rect())

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        sys.exit(0)

class MainUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Elements
        self.textField = QLineEdit('Sample Text')
        self.btn1 = QPushButton('Button 1')
        self.btn2 = QPushButton('Button 2')
        self.btn3 = QPushButton('Button 3')
        self.btn4 = QPushButton('Button 4')

    def init(self, screenSize):
        # Grid layout
        self.setLayout(QGridLayout())

        # Add elements
        # addWidget(widget, row, col, size of rows, size of cols)
        self.layout().addWidget(self.textField, 0, 0, 1, 2)
        self.layout().addWidget(self.btn1, 1, 0, 1, 1)
        self.layout().addWidget(self.btn2, 1, 1, 1, 1)
        self.layout().addWidget(self.btn3, 2, 0, 1, 1)
        self.layout().addWidget(self.btn4, 2, 1, 1, 1)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.init()

    # Screen size
    rect = App.primaryScreen().availableGeometry()
    widgetY = rect.height() / 10
    widgetW = rect.width() * 0.7

    # Create widget for UI, add it to main window
    mainUI = MainUI(window)
    mainUI.init(rect)

    # Size and center the widget
    mainUI.setGeometry(QRect(0,0,widgetW,200))
    qr = mainUI.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    mainUI.move(qr.topLeft().x(), widgetY)

    window.showFullScreen()
    # Optional styling
    #App.setStyle(QStyleFactory.create('Fusion'))
    sys.exit(App.exec())