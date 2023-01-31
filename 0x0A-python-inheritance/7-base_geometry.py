#!/usr/bin/python3
"""adding more instances to class"""


class BaseGeometry():
    """adding more instances"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greather than 0".format(name))
