import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget


class MyButton(QPushButton):
    def __init__(self, widget, value):
        super().__init__(parent=widget)
        self.value = value

        self.clicked.connect(self.intern)

    def intern(self):
        print("value = ", self.value)


class Test(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.setWindowTitle("test")
        self.setFixedSize(500, 500)

        button1 = QPushButton(self.widget)
        button1.setText("Button 1")
        button1.move(64, 32)
        button1.clicked.connect(self.button_clicked)

        button2 = MyButton(self.widget, "test")
        button2.setText("Button 2 ")
        button2.move(64, 62)

        button3 = QPushButton(self.widget)
        button3.setText("Button 3")
        button3.move(64, 92)
        button3.clicked.connect(
            lambda state, value="button 3": self.button_clicked3(value))

    def button_clicked(self):
        print("click")

    def button_clicked3(self, value):
        print('click 3 = ', value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Test()
    win.show()

    sys.exit(app.exec_())
