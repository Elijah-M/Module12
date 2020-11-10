"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/9/2020
This program is used for testing abstract classes
"""
from abc import ABC, abstractmethod


# Added a custom exception - this is what was missing
class InvalidSideError(Exception):
    """Raises an error when the length or width is invalid"""
    pass


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.num_sides = 3

    # overrides abstract method with implementation
    def area(self):
        return self.length * self.width

    def __str__(self):
        return str(self.area())


# Driver code
r = Rectangle(2, 3)
print(str(r))

# Garbage collection
del r
