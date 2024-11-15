"""Defines the rectangle class"""

class Rectangle:
    #TODO: define two field variables for length and width with values 100 and 200
    def __init__(self, length = 100, width = 200):
        self._length = length
        self._width = width

    def getLength(self):
        return self._length
    
    def setLength(self, newLength):
        self._length = newLength

    def getWidth(self):
        return self._width
    
    def setWidth(self, newWidth):
        self._width = newWidth

    def expandRectangle(self, lengthDelta, widthDelta):
        self._length += lengthDelta
        self._width += widthDelta

    def contractRectangle(self, lengthDelta, widthDelta):
        self._length -= lengthDelta
        self._width -= widthDelta

    def calculateArea(self):
        area = self._length * self._width
        return area