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

#5. Convert kilometers to miles
# 1km = 0.621 miles
km = int(input("Enter the distance in km: "))
miles = km*0.621
print("Distance is", miles, "miles")

#6. Calculate the displacement
'''
Write a Python program to calculate the displacement (d) of an object using the second equation of motion:
d =  ( v * v  -  u * u ) / (2 * a)
Where:
• v = Final velocity
• u = Initial velocity
• a = Acceleration
'''

v= int(input("Enter the Final velocity: "))
u= int(input("Enter the Initial velocity: "))
a= int(input("Enter the Acceleration: "))
d= (v**2-u**2)/(2*a)
print("Displacement is", d)

