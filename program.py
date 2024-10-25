"""Defines the program class that runs and creates shapes"""

from shape import Shape
from circle import Circle
from rectangle import Rectangle

class Program:
    def run(self):
        #create a circle object (instance of the class Circle)
        circle  = Circle()

        #print the radius of the default circle
        print(f"The default circle has the radius: {circle._radius}")

        #create a large circle
        largeCircle = Circle(1000)

        #print th eradius of the large circle
        print(f"The large circle has the radius: {largeCircle._radius}")

        #contract the circle by 20 pixels
        largeCircle.contractCircle(20)

        #calculate and print the area of the large circle
        largeCircleArea = largeCircle.calculateArea()
        print(f"The area of the large circle after contraction is: {largeCircleArea}.")

        #TODO: create a rectangle object
        rect = Rectangle()        

        #TODO:print its length and width
        print (f"This rectangle is {rect._length} by {rect._width}")

        #create a small rectangle that is 5x7
        smallRect = Rectangle(5, 7)

        #print the dimensions of the small rectangle
        print(f"The small rectangle has the dimensions: {smallRect._length} x {smallRect._width}.")

        #increase the small rectangle by 10 and 13
        smallRect.expandRectangle(10, 13)

        #calculate and print the area of the small rectangle
        smallRectArea = smallRect.calculateArea()
        print(f"The area of the small rectangle after contraction is {smallRectArea}")
    