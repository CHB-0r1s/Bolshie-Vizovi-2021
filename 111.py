import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 300)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Диаметр оболочки, м")
        self.name_label1.move(40, 40)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(200, 40)

        self.name_label2 = QLabel(self)
        self.name_label2.setText("Длина уголка, мм")
        self.name_label2.move(40, 80)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(200, 80)

        self.name_label3 = QLabel(self)
        self.name_label3.setText("Толщина стенок стрингера, мм")
        self.name_label3.move(40, 120)

        self.name_input3 = QLineEdit(self)
        self.name_input3.move(200, 120)

        self.name_label4 = QLabel(self)
        self.name_label4.setText("Количество стрингеров, шт")
        self.name_label4.move(40, 160)

        self.name_input4 = QLineEdit(self)
        self.name_input4.move(200, 160)

        self.label = QLabel(self)
        self.label.resize(150, 50)
        self.label.move(160, 200)

        self.btn = QPushButton('Посчитать', self)
        self.btn.resize(100, 50)
        self.btn.move(40, 200)
        self.btn.clicked.connect(self.func)

    def func(self):
        try:
            x1 = float(self.name_input1.text())
            x2 = float(self.name_input2.text())
            x3 = float(self.name_input3.text())
            x4 = float(self.name_input4.text())


            if x1 == 1.6:
                x11 = 0
            elif x1 < 1.6:
                x11 = (1.6 - x1) / 0.4 * (-1)
            elif x1 > 1.6:
                x11 = (x1 - 1.6) / 0.4
            if x2 == 30:
                x22 = 0
            elif x2 < 30:
                x22 = (30 - x2) / 10 * (-1)
            elif x2 > 30:
                x22 = (x2 - 30) / 10
            if x3 == 4:
                x33 = 0
            elif x3 < 4:
                x33 = (4 - x3) / 1 * (-1)
            elif x3 > 4:
                x33 = (x3 - 4) / 1
            if x4 == 6:
                x44 = 0
            elif x4 < 0:
                x44 = (6 - x4) / 2 * (-1)
            elif x4 > 0:
                x44 = (x4 - 6) / 2

            a = []
            a.append(x11)
            a.append(x22)
            a.append(x33)
            a.append(x44)


            b0 = 1.1168
            b1 = -0.0229
            b2 = 0.07387
            b3 = 0.03562
            b4 = 0.10858
            b12 = -0.0031
            b13 = 0.01026
            b14 = -0.0132
            b123 = 0.01108
            b134 = 0.00397
            b1234 = 0.00697
            b23 = 0.02707
            b24 = 0.03138
            b234 = 0.00993
            b34 = 0.02341
            b124 = 0.00034


            y = b0 + b1 * a[0] + b2 * a[1] + b3 * a[2] + b4 * a[3] + b12 * a[0] * a[1] + b13 * a[0] * a[2] + b14 * a[0] * a[3] + b123 * a[0] * a[1] * a[2] + b134 * a[0] * a[2] * a[3] + b1234 * a[0] * a[1] * a[2] * a[3] + b23 * a[1] * a[2] + b24 * a[1] * a[3] + b234 * a[1] * a[2] * a[3] + b34 * a[2] * a[3] + b124 * a[0] * a[1] * a[3]



            self.label.setText('')
            self.label.setText(f"Выдерживаемая нагрузка {y}")
            print(y)
        except:
            self.label.setText('')
            self.label.setText('Введите 4 числа')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
