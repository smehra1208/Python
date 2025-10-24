#1. WAP Area of Rectangle
length = flaot(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
Area = length*breadth
print("Area of rectangle is", Area)

#2. WAP Area of Triangle
base = float(input("Enter base of the triangle: "))
height= float(input("Enter height of the triangle: "))
Area = (1/2)*base*height
print("Area of triangle is", Area)

#3. WAP Area of Trapezium
a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
height= int(input("Enter height of the trapezium: "))
Area = (1/2)*(a+b)*height
print("Area of trapezium is", Area)

#4. WAP Area of Circle
import math
radius = float(input("Enter radius of circle: "))
Area = math.pi*radius**2
print("Area of circle is", Area)

#5. WAP Convert kilometers to miles
# 1km = 0.621 miles
km = float(input("Enter the distance in km: "))
miles = km*0.621
print("Distance is", miles, "miles")

#6. WAP Calculate the displacement
#Write a Python program to calculate the displacement (d) of an object using the second equation of motion:
#d =  ( v * v  -  u * u ) / (2 * a)
#Where:
#• v = Final velocity
#• u = Initial velocity
#• a = Acceleration

v= float(input("Enter the Final velocity: "))
u= float(input("Enter the Initial velocity: "))
a= float(input("Enter the Acceleration: "))
d= (v**2-u**2)/(2*a)
print("Displacement is", d)

#7. WAP Surface Area of a Cuboid
length = float(input("Enter length of cuboid: "))
breadth = float(input("Enter breadth of cuboid: "))
height = float(input("Enter height of cuboid: "))
surface_area = 2*((length*breadth)+(breadth*height)+(height*length))
print("Surface area of cuboid is", surface_area)

#8. WAP Find roots of Quadratic equation
import math
a = int(input("Enter value of first constant 'a': "))
b = int(input("Enter value of second constant 'b': "))
c = int(input("Enter value of third constant 'c': "))
root1= (-b + math.sqrt(b**2-4*a*c))/(2*a)
root2= (-b - math.sqrt(b**2-4*a*c))/(2*a)
print("Roots of quadratic equation are", root1, "and", root2)

#9. WAP Check whether a number is positive or negative
a= float(input("enter a number: "))
if a<0:
    print("Number is negative")
else:
    print("Number is positive")

#10. WAP Check if the number is odd or even.
num= int(input("Enter a number: "))
if num%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#11. WAP Check eligibility to vote
age=int(input("Enter your age: "))
if age>= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#12. WAP Eligibility to work (if age is between 18 and 60)
age=int(input("Enter your age: "))
if age>=18 and age<60:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")

#13. WAP Check Valid marks (between 0 to 100)
marks=float(input("Enter your marks: "))
if marks>=0 and marks<=100:
    print("valid marks.")
else:
    print("invalid marks.")

#14. WAP: Gender Check
gender = input("Enter your gender: ").lower()
if gender=="m":
    print("Gender is male.")
else:
    print("Gender is female.")

#15. WAP: Check if the alphabet is vowel or consonant
alphabet = input("Enter a alphabet: ").lower()
if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
    print("Alphabet is a vowel.")
else:
    print("Alphabet is a consonant.")

#16. WAP: check exam result (passing marks = 45, should pass in all subjects - maths, physics, chemistry)
maths=float(input("Enter marks in maths: "))
phy = float(input("Enter marks in physics: "))
chem = float(input("Enter marks in chemistry: "))
if maths>=45 and phy>=45 and chem>=45:
    print("passed")
else:
    print("failed")