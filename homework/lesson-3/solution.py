#1. Basic Arithmetic Operations
value1 = int(input("please enter your first value:"))
value2 = int(input("please enter your second value:"))
print("First value:", value1)
print("Second value:", value2)
print("Addition:", value1 + value2)
print("Subtraction:", value1 - value2)
print("Multiplication:", value1 * value2)
print("Division:", value1 / value2)

#2. Modulus and Exponentiation
number = int(input("Please enter a lucky number:"))
print("Your lucky number is", number)
print("The remainder when divided by 3 equals:", number % 3)
print("Your number to the power of two equals:", number ** 2)

#3. Odd or Even
if number % 2 == 0: 
    print("Your number is even.")
else:
    print("Your number is odd.")

#4. Compare Two Numbers
number1 = int(input("Please enter a new first value"))
number2 = int(input("Please enter a new second value"))
print("Your new first value is:", number1)
print("Your new second value is:", number2)
if number1 > number2:
    print("Your new first value is greater than your new second value.")
if number2 > number1:
    print("Your new second value is greater than your new first value.")
if number1 == number2:
    print("Your new values are equal.")

#5. Print Numbers 1 to 10  
for number in range(1, 11):
    print(number)

#6. Multiplication Table

multiplication = int(input("Please enter a number to know the multiplication table from 1 to 10:"))
for multiplication10 in range(1, 11):
    print(multiplication, "x", multiplication10, "=", multiplication * multiplication10)

#7. FizzBuzz
for num20 in range(1, 21): 
    if num20 % 3 == 0:
        print("Fizz")
    elif num20 % 5 == 0:
        print("Buzz")
    if   num20 % 3 == 0 and num20 % 5 == 0:
        print("FizzBuzz")
    else: print(num20)
    
#8. Leap year
year = int(input("Please enter a year:"))
print("The year you chose is:", year)
if year % 4 == 0 and year % 100 != 0 or year % 100 ==0:
    print(year, "is a leap year.")
else: print(year, "is not a leap year.")

