#1. WAP To check the temperature
temp=float(input("Enter the temperature: "))
if temp==25:
    print("Normal")
elif temp<25:
    print("Cold")
else:
    print("Hot")

#2. WAP To generate discounted bill. If bill is less than $1000 - get 10% discount
#   for amount $1000 to $5000, you get a 15% discount
#   for amount $5000 to $10000, you get 20% discount
#   for amount equal to or greater than $10000, you get 25% discount

bill = float(input("Enter your bill amount: "))
if bill<1000:
    bill*=0.90
elif bill>=1000 and bill<5000:
    bill*=0.85
elif bill>=5000 and bill<10000:
    bill*=0.80
else:
    bill*=0.75
print("Your bill after discount is", bill)

#3. WAP Day Number to Day Name
day_number=int(input("Enter the day number: "))
if day_number==0:
    print("Monday")
elif day_number==1:
    print("Tuesday")
elif day_number==2:
    print("Wednesday")
elif day_number==3:
    print("Thursday")
elif day_number==4:
    print("Friday")
elif day_number==5:
    print("Saturday")
elif day_number==6:
    print("Sunday")
else:
    print("Enter Valid day number")

#4. WAP Month number to month name
month_num=int(input("enter the month number: "))
if month_num==1:
    print("January")
elif month_num==2:
    print("February")
elif month_num==3:
    print("March")
elif month_num==4:
    print("April")
elif month_num==5:
    print("May")
elif month_num==6:
    print("June")
elif month_num==7:
    print("July")
elif month_num==8:
    print("August")
elif month_num==9:
    print("September")
elif month_num==10:
    print("October")
elif month_num==11:
    print("November")
elif month_num==12:
    print("December")
else:
    print("Enter valid month number")

#5. WAP (single) Digits to Words
digit = int(input("Enter the digit: "))
if digit == 0:
    print("Zero")
elif digit == 1:
    print("One")
elif  digit == 2:
    print("Two")
elif  digit == 3:
    print("Three")
elif  digit == 4:
    print("Four")
elif  digit == 5:
    print("Five")
elif  digit == 6:
    print("Six")
elif  digit == 7:
    print("Seven")
elif  digit == 8:
    print("Eight")
elif  digit == 9:
    print("Nine")
else:
    print("Enter valid digit number")