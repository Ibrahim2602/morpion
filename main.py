"""
TODO
"""

import sys
from PyQt5.QtWidgets import QApplication


# class MyButton(QPushButton):
#     def __init__(self, widget, value, text):
#         super().__init__(parent=widget)
#         self.value = value
#         self.clicked.connect(self.click2)
#         self.setText(text)

#     def click2(self):
#         print(self.value)


# class Test(QMainWindow):
#     """
#     TODO
#     """

#     def __init__(self):
#         super().__init__()

#         self.widget = QWidget()
#         self.setCentralWidget(self.widget)

#         self.setFixedSize(500, 500)
#         self.setWindowTitle("Test")

#         button1 = QPushButton(self.widget)
#         button1.setText("button 1")
#         button1.move(100, 100)
#         button1.clicked.connect(self.click1)

#         button2 = MyButton(self.widget, "click 2", "button 2")
#         button2.move(100, 150)

#         button3 = QPushButton(self.widget)
#         button3.setText("button 3")
#         button3.move(100, 200)
#         button3.clicked.connect(
#             lambda state, value="click 3": self.click3(value))

#     def click1(self):
#         print("click 1")

#     def click3(self, value):
#         print(value)


from model.morpionModel import MorpionModel
from view.morpionView import MorpionView
from controller.morpionController import MorpionController

app = QApplication(sys.argv)

model = MorpionModel()
view = MorpionView()
controller = MorpionController()

model.addView(view)

view.setModel(model)
view.setController(controller)

controller.setModel(model)
controller.setView(view)

# window = Test()
# window.show()

view.show()

sys.exit(app.exec_())
