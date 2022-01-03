"""
TODO
"""

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QMenu, QAction, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QSize, Qt


class MorpionView(QMainWindow):
    """
    TODO
    """

    def __init__(self):
        """
        TODO
        """
        super().__init__()

        self.setWindowTitle("Morpion")
        self.setFixedSize(500, 500)
        self.statusBar().showMessage("Player:")

        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        self.__gridLayout = QGridLayout()
        self.__window.setLayout(self.__gridLayout)
        self.__gridButton = []

        self.__model = None
        self.__controller = None

        menuBar = self.menuBar()
        gameMenu = QMenu("&Jeu", self)
        menuBar.addMenu(gameMenu)

        helpMenu = QAction("&Help", self)
        helpMenu.triggered.connect(self.helpView)
        menuBar.addAction(helpMenu)

        restart = QAction(self)
        restart.setText("&Restart")
        gameMenu.addAction(restart)
        restart.triggered.connect(self.restart)

        exitProgram = QAction(self)
        exitProgram.setText("&Quit")
        gameMenu.addAction(exitProgram)
        exitProgram.triggered.connect(self.close)

        rect = self.geometry()
        w = rect.width() / 3
        h = rect.width() / 3

        crossImage = QImage("elements.png", 'png').copy(370, 0, 400, 350)
        roundImage = QImage("elements.png", 'png').copy(30, 0, 400, 350)

        self.__cross = QIcon(QPixmap.fromImage(crossImage).scaled(w, h))
        self.__round = QIcon(QPixmap.fromImage(roundImage).scaled(w, h))

        for i in range(3):
            tmp = []
            for j in range(3):
                button = QPushButton(parent=self.__window)
                button.setIconSize(QSize(w-40, h-20))
                button.setStyleSheet(
                    "border: 1px solid blue;background-color:rgba(0, 0, 238, 0.4)")
                button.setFixedSize(w - 10, h-10)
                tmp.append(button)
                button.clicked.connect(
                    lambda state, vi=i, vj=j: self.actionCalled(vi, vj))
                self.__gridLayout.addWidget(button, i, j)

            self.__gridButton.append(tmp)

    def helpView(self):
        """
        TODO
        """
        dialog = QDialog()
        dialog.setAttribute(Qt.WA_DeleteOnClose)
        dialog.setWindowTitle("Help")

        label = QLabel("<h1> J'ai besoin d'aide </h1>", parent=dialog)
        label.show()
        dialog.exec_()

    def actionCalled(self, l, c):
        """
        TODO
        """
        self.__controller.play(l, c)

    def setModel(self, model):
        """
        TODO
        """
        self.__model = model

    def cleanView(self):
        """
        TODO
        """
        for lbutton in self.__gridButton:
            for button in lbutton:
                button.setIcon(QIcon())

    def restart(self):
        """
        TODO
        """
        self.__controller.restartGame()

    def setController(self, controller):
        """
        TODO
        """
        self.__controller = controller

    def setWinner(self, player):
        """
        TODO
        """
        self.statusBar().showMessage(player + " a gagné!")

    def setPlayer(self, player):
        """
        TODO
        """
        self.statusBar().showMessage(player + " doit jouer")

    def updateView(self, changes):
        """
        TODO
        """
        for change in changes:
            i = change[0]
            j = change[1]

            button = self.__gridButton[i][j]
            if self.__model.get(i, j) == 'x':
                button.setIcon(self.__cross)
            elif self.__model.get(i, j) == 'o':
                button.setIcon(self.__round)
