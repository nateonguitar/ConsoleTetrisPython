import numpy
from game.vector2 import Vector2
from game.game_object import GameObject


class Shape(GameObject):
    char = '▣'

    def __str__(self):
        return 'Shape'


class Square(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [1, 1],
            [1, 1],
        ]

    def __str__(self):
        return 'Square'

class Line(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [1],
            [1],
            [1],
            [1],
        ]

    def __str__(self):
        return 'Line'


class ForwardsL(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [1, 0],
            [1, 0],
            [1, 1],
        ]

    def __str__(self):
        return 'ForwardsL'


class BackwardsL(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 1],
            [0, 1],
            [1, 1],
        ]

    def __str__(self):
        return 'BackwardsL'


class ForwardsZ(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [1, 1, 0],
            [0, 1, 1],
        ]

    def __str__(self):
        return 'ForwardsZ'


class BackwardsZ(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 1, 1],
            [1, 1, 0],
        ]

    def __str__(self):
        return 'BackwardsZ'


class TShape(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 1, 0],
            [1, 1, 1],
        ]

    def __str__(self):
        return 'TShape'
