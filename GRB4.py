# FILE: 2252_AhmedAbdirahman_GRBLesson04.py
# NAME: Dice Rolling Simulator
# AUTHOR(s): Abdirahman Ahmed
# DATE: 10/17/2024


import random  # Importing random module to generate random numbers

def roll_dice(sides=6):
    return random.randint(1, sides)  

def dice_simulator():
    while True: 
        print("Rolling the dice...")
        result = roll_dice()  
        print(f"You rolled a {result}")  

        
        choice = input("Do you want to roll again? (yes/no): ").lower()

        if choice != 'yes':  # Exit if the user doesn't want to roll again
            print("Thanks for playing!")
            break  # Stop the loop, ending the program

dice_simulator()  # Run the dice rolling function


import random  # Importing random module to generate random numbers

def generate_numbers():
    num1 = random.randint(1, 999)  
    num2 = random.randint(1, 999)  
    return num1, num2 

def math_quiz():
    while True:  
        num1, num2 = generate_numbers()  
        print(f"  {num1}")
        print(f"+ {num2}")
        print("-----")
        
        # Ask the user for their answer
        user_answer = int(input("Enter your answer: "))
        correct_answer = num1 + num2  # Calculate the correct answer
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Congratulations! That's correct.")  
        else:
            print(f"Oops! The correct answer was {correct_answer}.")  
            
        # Ask the user if they want to try again
        choice = input("Do you want to try another problem? (yes/no): ").lower()

        if choice != 'yes':  # Exit if the user doesn't want to continue
            print("Thanks for playing!")
            break  # Stop the loop, ending the program



#2. Math Quiz Program

import random  # Importing random module to generate random numbers

def generate_numbers():
    num1 = random.randint(1, 999)  # Generate a random number between 1 and 999
    num2 = random.randint(1, 999)  # Generate another random number
    return num1, num2  # Return both numbers

def math_quiz():
    while True:  # Loop to keep showing math problems until user chooses to stop
        num1, num2 = generate_numbers()  # Generate two random numbers
        print(f"  {num1}")
        print(f"+ {num2}")
        print("-----")
        
        # Ask the user for their answer
        user_answer = int(input("Enter your answer: "))
        correct_answer = num1 + num2  # Calculate the correct answer
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Congratulations! That's correct.")  # Congratulate if correct
        else:
            print(f"Oops! The correct answer was {correct_answer}.")  # Show correct answer if wrong

        # Ask the user if they want to try again
        choice = input("Do you want to try another problem? (yes/no): ").lower()

        if choice != 'yes':  
            print("Thanks for playing!")
            break  # Stop the loop, ending the program

math_quiz()  # Run the math quiz function


