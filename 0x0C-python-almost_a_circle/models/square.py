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
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string reperstintion of square object"""
        ob_id = self.id
        ob_x = self.x
        ob_y = self.y
        ob_size = self.size
        return "[Square] ({}) {}/{} - {}".format(ob_id, ob_x, ob_y, ob_size)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update object attributes"""
        if not args:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
            return (0)

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
            self.height = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
