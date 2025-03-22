#Exercise

score = int(input("please enter your score"))

if score > 90:
    print("A")
elif score > 80 and score <= 90:
    print("B")
elif score >= 60 and score <= 80:
    print("C")
elif score < 60:
    print("D")

numbers=1
for number in range(1, 101):
    print(number)
for odd in number:
    if odd % 2 != 0:
       print(odd)



name=input("Please state your name")
print("Good day", name)
#output: Good day Amanda
lastname=input("Please tell me your last name")
print("Good day", lastname)
#output: Good day Amanda
number1 = int(input("please enter your first value"))
number2 = int(input("please enter your second value"))
print(number1+number2)