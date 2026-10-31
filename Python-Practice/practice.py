#1 User will input (3ages).Find the oldest one
'''
age1 = int(input("Enter THe First Age : "))
age2 = int(input("Enter THe Second Age : "))
age3 = int(input("Enter THe Third Age : "))

if age1 < 0 or age2 < 0 or age3 < 0 :
    print("Invalid Age")
    print("Age can't be negative")

else: 
    if age1 >= age2 and age1 >= age3 :
     print(age1)

    elif age2 >= age3 and age2 >= age1 :
     print(age2)

    else : 
     print(age3)
'''

#2 Write a program that will convert celsius value to fahrenheit
'''
celsius = int(input("Enter the temperature in celsius : "))


Fahrenheit = (celsius * (9/5))+32


print(f"{Fahrenheit} degree fahrenheit")
'''

#3 User will input (2numbers).Write a program to swap the numbers
'''
no1 = int(input("enter the first number: "))
no2 = int(input("enter the second number: "))

no1, no2 = no2, no1
print(no1, no2)
'''

#4 Write a program that will give you the sum of 3 digits
'''
no1 = int(input("enter the first number: "))
no2 = int(input("enter the second number: "))
no3 = int(input("enter the third number: "))

print(no1+ no2+ no3)
'''

#5 Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
'''
num = input("enter a four digit number: ")

reverse = num[::-1]

print(reverse)

if num == reverse :
    print("reverse is true (Palindrome)")

else :
    print("reverse is false (Not a Palindrome)")
'''

#6 Write a program that will tell whether the number entered by the user is odd or even.
'''
number = int(input("Enter the number: "))

if number % 2 == 0 :
    print("the number entered by the user is even")

else :
    print("the number entered by the user is odd")
'''

#7 Write a program that will tell whether the given year is a leap year or not.
'''
year = int(input("Enter the year: "))

if year % 4 == 0 or year % 400 == 0 :
    print("It is a leap year.")

else :
    print("It is not a leap year.")
'''

#8 Write a program to find the euclidean distance between two coordinates.
'''
import math

x1 = int(input("Enter the Point A x1 value: "))
x2 = int(input("Enter the Point A x2 value: "))
y1= int(input("Enter the Point B y1 value: "))
y2 = int(input("Enter the Point B y2 value: "))

distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

print(distance)
'''

#9 Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
'''
angle1 = int(input("enter the first angle: "))
angle2 = int(input("enter the second angle: "))
angle3 = int(input("enter the third angle: "))

if (angle1 + angle2 + angle3 == 180) :
    print("It can form a triangle")

else:
    print("It can not form a triangle")
'''

#10 Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
'''
buy = int(input("Enter the Cost Price in Rupees: "))
sell = int(input("Enter the Selling Price in Rupees: ")) 

if sell > buy :
    print(f"Its a Profit of {sell - buy} Rupees")

elif buy > sell:
    print(f"Its a Loss of {buy - sell} Rupees")

else :
    print("Its neither Loss nor Profit")
'''

#11 Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
'''
import math
r = int(input("Enter the radii of circular base: "))
h = int(input("Enter the height of cylinder: "))

volume = math.pi* r**2 *h
litre = volume/ 1000 #assuming volume is in cm
milk = litre* 40

print(f"{volume:.2f}cm³")
print(f"after converting volume into litre it give {litre:.2f} litre")
print(f"The cost of {litre:.2f} litre milk is {milk:.2f}")
'''

#12 Write  a program that will tell whether the given number is divisible by 3 & 6.
'''
n = int(input("Enter the Number: "))

if n % 3 == 0 and n % 6 == 0 :
    print(f"{n} is divisible by 3 & 6")

elif n % 3 == 0 or n % 6 == 0 :
    if n % 3 == 0 and n % 6 != 0 :
        print(f"{n} is divisible 3 but not divisible by 6")
    elif n % 6 == 0 and n % 3 != 0 :
        print(f"{n} is divisible 6 but not divisible by 3")
    else :
        print("Not divisible by 3 or 6")

else :
    print("Not divisible by 3 or 6")
'''

#13 Write a program that will take three digits from the user and add the square of each digit.
'''
a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))
c = int(input("Enter the Number: "))

print(a**2 + b**2 + c**2)
'''

#14 Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
'''
p = int(input("Enter the value of principle: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period: "))

SI = (p * r * t)/100
print(SI)
'''

#15 Write a program that will check whether the number is armstrong number or not.
'''
f = int(input("Enter the first Number: "))
e = int(input("Enter the second Number: "))
d = int(input("Enter the third Number: "))

num = f*100 + e*10 + d

if (num == f**3 + e**3 + d**3 ) :
    print("The number is armstrong number")

else:
    print("The number is not an armstrong number")
'''

#16 Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.
'''
x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))
z = int(input("Enter a Number: "))

num = w*1000 + x*100 + y*10 + z

if (num == w**4 + x**4 + y **4 + z**4) :
    print("The number is a narcissist number.")

else :
    print("The number is not a narcissist number")
'''

#17 Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit
'''
while True:

   print("\nEnter your Choice ")
   print("1. convert cm to ft")
   print("2. convert kl to miles")
   print("3. convert usd to inr")
   print("4. exit")

   choice = int(input("Enter your choice: "))


   if (choice == 1) :
       cm = int(input("Enter the length in cm: "))
       ft = cm / 30.48
       print(f"Length in feet: {ft:.2f} ft" )

   elif (choice == 2):
       kl = int(input("Enter the distance in kl: "))
       miles = kl * 0.621371
       print(f"Distance in miles: {miles:.2f} miles")

   elif (choice == 3) :
       usd = int(input("Enter the amount in usd: "))
       inr = usd * 95.16
       print(f"Amount in Indian currency: {inr:.2f} inr")

   elif (choice == 4) :
       print("Exit the program. ")
       break
   else :
       print("Try Again")
'''

#18 Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
'''
head = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))

dog = (legs-(2*head))/ 2
chick = head - dog
print(f"The total number of dogs: {dog} \nThe total number of chickens: {chick} ")
'''

#19 Write a program that will swap numbers
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a,b = b,a

print("a=", a)
print("b=", b)
'''

#20 Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.
'''
n = int(input("Enter the value of n: "))
    
sum = (n*(n+1))/2
    
print(f"The sum of first n numbers: {sum}")
'''

