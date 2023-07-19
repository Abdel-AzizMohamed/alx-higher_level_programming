#!/usr/bin/python3
"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """initalize a new object

            Args:
                size(int): size of the square
                x(int): x-axis of the square
                y(int): y-axis of the square
                id(int): id of the square
        super().__init__(size, size, x, y, id)
        """

    def __str__(self):
        """return a string reperstintion of square object"""
        ob_id = self.id
        ob_x = self.x
        ob_y = self.y
        ob_size = self.width
        return "[Square] ({}) {}/{} - {}".format(ob_id, ob_x, ob_y, ob_size)
