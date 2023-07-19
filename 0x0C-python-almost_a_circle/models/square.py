#!/usr/bin/python3
"""Define square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ob_id = self.id
        ob_x = self.x
        ob_y = self.y
        ob_size = self.width
        return "[Square] ({}) {}/{} - {}".format(ob_id, ob_x, ob_y, ob_size)
