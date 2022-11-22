import random
import sys

from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtCore

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.is_drawing = False
        self.coords = (0,0)
        self.radius = 0

    def draw_circle(self):
        self.is_drawing = True
        self.coords = (random.randint(20, 300), random.randint(20, 300))
        self.radius = random.randint(2,60)
        self.update()

    def paintEvent(self, event) -> None:
        if self.is_drawing:
            painter = QPainter(self)
            painter.begin(self)
            pen = QPen(QColor('yellow'))
            pen.setWidth(5)
            painter.setPen(pen)

            painter.drawEllipse(*self.coords, self.radius, self.radius)
            painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    sys.exit(app.exec())