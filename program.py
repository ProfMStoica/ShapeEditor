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

        #ask the user to create two circles of the different radiuses and compare them. How?
        #ask the user for the radius of the first circle
        radiusOne = float(input("Please enter the radius of the first circle: "))

        #create the first circle
        circleOne = Circle(radiusOne)

        #ask the user for the radius of the second circle
        radiusTwo = float(input("Please enter the radius of the second circle: "))

        #create the second circle
        circleTwo = Circle(radiusTwo)

        #let the user know which ones is larger. How?
        #calculate the areas of the two circles
        areaOne = circleOne.calculateArea()
        areaTwo = circleTwo.calculateArea()

        #compare the areas to determine which is one is larger
        if areaOne > areaTwo:
            print("The first circle is larger")
        elif areaTwo > areaOne:
            print ("The second circle is larger")
        else:
            print("The circles have the same area")

        #TODO: add user interactivity to allow the user to create
        #rectangles of different dimensions and compare them

        
    