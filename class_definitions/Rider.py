"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/9/2020
This program is used for testing abstract classes
"""
from abc import ABC, abstractmethod


class Rider(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def power_source(self):
        pass


class Bicycle(Rider):
    
    def power_source(self):
        print("Human Powered, not enclosed\n", "1 or 2 if tandem or a daredevil")


class Motorcycle(Rider):
    def power_source(self):
        print("Engine Powered, not enclosed\n", "1 or 2")


class Car(Rider):
    def power_source(self):
        print("Engine Powered, not enclosed\n", "1 plus comfortably")


# Driver
b = Bicycle('')
m = Motorcycle('')
c = Car('')
b.power_source()
m.power_source()
c.power_source()

# Garbage collection
del b, m, c
