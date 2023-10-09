#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent the base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.

        Args:
            name (str): this is the name of the parameter.
            value (int): This is the parameter to validate.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
