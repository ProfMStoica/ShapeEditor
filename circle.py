"""Defines the circle class"""
import  math

class Circle:
    """Constructor for circle objects"""
    def __init__(self, radius = 10):
        self._radius = radius

    def getRadius(self):
        return self._radius
    
    def setRadius(self, newRadius):
        self._radius = newRadius
        
    def expandCircle(self, radiusDelta):
        self._radius = self._radius + radiusDelta

    def contractCircle(self, radiusDelta):
        self._radius = self._radius - radiusDelta

    def calculateArea(self):
        area = self._radius**2 * math.pi
        return area
