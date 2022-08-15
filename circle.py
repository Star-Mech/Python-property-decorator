import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def create_instance(cls, radius):
        return cls(radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    # @diameter.setter
    # def diameter(self, value):
    #     self.radius = value / 2
