"""
TODO
"""


class MorpionController:
    
    def __init__(self):
        """
        TODO
        """
        self.__model = None
        self.__view = None
        self.__player = 0
        self.__winner = None

    def setModel(self, model):
        """
        TODO
        """
        self.__model = model

    def setView(self, view):
        """
        TODO
        """
        self.__view = view
        self.__view.setPlayer("x")

    def play(self, l, c):
        """
        TODO
        """
        if self.__winner is not None or self.__model.get(l, c) != ' ':
            return

        player = ('x', 'o')[self.__player % 2]
        self.__model.set(l, c, player)

        isWinner = False

        for i in range(3):
            isWinner = isWinner or (self.__model.get(i, 0) == player and self.__model.get(
                i, 1) == player and self.__model.get(i, 2) == player)

            isWinner = isWinner or (self.__model.get(0, i) == player and self.__model.get(
                1, i) == player and self.__model.get(2, i) == player)

        isWinner = isWinner or (self.__model.get(0, 0) == player and self.__model.get(
            1, 1) == player and self.__model.get(2, 2) == player)
        isWinner = isWinner or (self.__model.get(2, 0) == player and self.__model.get(
            1, 1) == player and self.__model.get(0, 2) == player)

        if isWinner:
            self.__winner = player
            self.__view.setWinner(player)
        else:
            self.__player += 1
            self.__view.setPlayer(player)

    def restartGame(self):
        """
        TODO
        """
        self.__model.clear()
        self.__view.cleanView()

        self.__player = 0
        self.__winner = None
