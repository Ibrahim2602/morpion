"""
TODO
"""


class MorpionModel:
    """
    TODO
    """

    def __init__(self):
        """
        TODO
        """
        self.__views = []
        self.__matrix = [[' ', ' ', ' '] for i in range(3)]

    def clear(self):
        """
        TODO
        """
        self.__matrix = [[' ', ' ', ' '] for i in range(3)]

    def addView(self, view):
        """
        TODO
        """
        self.__views.append(view)

    def get(self, l, c):
        """
        TODO
        """
        assert l in (0, 1, 2) and c in (0, 1, 2)
        return self.__matrix[l][c]

    def set(self, l, c, v):
        """
        TODO
        """
        assert l in (0, 1, 2) and c in (0, 1, 2) and v in ('x', 'o')
        assert self.__matrix[l][c] == ' '
        self.__matrix[l][c] = v

        for view in self.__views:
            view.updateView([(l, c)])
