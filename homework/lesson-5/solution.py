#Homework exercise 1

from datetime import datetime

# Get current date and time
current_time = datetime.now()
print("Current date and time:", current_time)

#Homework exercise 2: Letter Count

# Function with print
def count_letters_print(text):
    count = 0
    for letter in text:
        if letter.isalpha():
            count += 1
    print("Number of letters:", str(count))

count_letters_print("Amanda")
count_letters_print("Am123an123da123")

# Function with return
def count_letters_return(text):
    count = 0
    for letter in text:
        count += 1
    return count

# Try both versions
count_letters_print("Hello")
letters = count_letters_return("Hello")
print("Returned value stored in variable:", letters)

#Homework exercise 3: Function results in another function

# a) Sum function
def sum_numbers(a, b):
    return a + b

# b) Save result
result = sum_numbers(5, 7)

# c) Function to check if divisible by 3
def check_divisible_by_3(number):
    if number % 3 == 0:
        print(f"{number} is divisible by 3")
    else:
        print(f"{number} is NOT divisible by 3")

# d) Call the second function with result
check_divisible_by_3(result)

#Homework exercise 4: Rock, paper, scissors
import random

def play_game(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.randint(0, 2)

    print(f"You chose: {options[user_choice]}")
    print(f"Computer chose: {options[computer_choice]}")

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

# Test the game
print(play_game(0))  # Try Rock
print(play_game(1))  # Try Paper
print(play_game(2))  # Try Scissors

#Exercise 4 version with strings
#import random
#def play_game1(user_choice1):
    #possible_move = ["Rock", "Paper", "Scissors"]
    #computer_move = random.choice(possible_move)

    #if computer_move == user_choice1
        #print("It's a tie!")
    #elif computer_move == "rock":
       # if user_choice1 == 