#!/usr/bin/python3
"""This defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """This Initialize a new square.

        Args:
            size (int): The size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)

