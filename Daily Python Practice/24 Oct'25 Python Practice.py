#1. WAP Area of Rectangle
length = int(input("Enter length of the rectangle: "))
breadth = int(input("Enter breadth of the rectangle: "))
Area = length*breadth
print("Area of rectangle is", Area)

#2. WAP Area of Triangle
base = int(input("Enter base of the triangle: "))
height= int(input("Enter height of the triangle: "))
Area = (1/2)*base*height
print("Area of triangle is", Area)

#3. WAP Area of Trapezium
a = int(input("Enter length of first side: "))
b = int(input("Enter length of second side: "))
height= int(input("Enter height of the trapezium: "))
Area = (1/2)*(a+b)*height
print("Area of trapezium is", Area)

#4. WAP Area of Circle
import math
radius = int(input("Enter radius of circle: "))
Area = math.pi*radius**2
print("Area of circle is", Area)