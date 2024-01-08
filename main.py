import random
import sys
from PyQt5 import uic
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.painting = False
        self.CirclesButton.clicked.connect(self.run)

    def run(self):
        self.painting = True
        self.update()

    def paintEvent(self, event):
        if self.painting:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.painting = False

    def draw_flag(self, qp):
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor(255, 255, 0))
        qp.setPen(pen)
        for i in range(15):
            razm = random.randint(50, 200)
            x, y = random.randint(10, 500), random.randint(10, 500)
            qp.drawEllipse(x, y, razm, razm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())