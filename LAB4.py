
# FILE: 2252_AhmedAbdirahman_GRBLesson04.py
# NAME: 
# AUTHOR(s): Abdirahman Ahmed
# DATE: 10/17/2024


import random

def get_computer_choice():
    # Generate a random number between 1 and 3
    choice = random.randint(1, 3)
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "scissors"
    else:
        return "paper"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    user_name = input("What's your name? ")

    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        computer_choice = get_computer_choice()

        user_choice = input(f"{user_name}, enter your choice (rock, paper, or scissors): ").lower()

        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            print(f"{user_name} wins this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie! Let's do it again.")
            continue  

        rounds_played += 1

        print(f"Score: {user_name} - {user_score} | Computer - {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Thanks for playing, {user_name}!")
    print(f"Total rounds played: {rounds_played}")
    print(f"Final Score: {user_name} - {user_score} | Computer - {computer_score}")

play_game()
