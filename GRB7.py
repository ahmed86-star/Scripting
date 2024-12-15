
#FILE: 2252_AAhmed_Lesson07_RandomNumberGenerator.py
# NAME: Random
# AUTHOR(s): Abdirahman Ahmed
# DATE: 11/26/2024
# PURPOSE:Generate a set of random numbers based on user input, store them in a file,and then display the numbers along with the lowest, highest, sum, and average.

import random

def header():
    print("Welcome to the Random Number Generator Program!")

def user_input():
    while True:
        try:
            num = int(input("Enter a number to generate random numbers: "))
            if num < 1:
                print("Please enter a number greater than 0.")
            else:
                return num
        except ValueError:
            print("Invalid input! Please enter a whole number.")

# Function to generate random numbers and save them to a file
def generate_numbers(num):
    number_list = [random.randint(0, 50) for _ in range(num)]  
    with open("random_numbers.txt", "w") as file:
        file.write("\n".join(map(str, number_list))) 

    return number_list 

# Function to display results to the user
def display_results(numbers):
    print("Generated numbers:", numbers)
    print("Lowest number:", min(numbers))
    print("Highest number:", max(numbers))
    print("Sum of numbers:", sum(numbers))
    print("Average of numbers:", sum(numbers) / len(numbers))

def main():
    header()  
    num = user_input()  
    numbers = generate_numbers(num)  
    display_results(numbers)  

if __name__ == "__main__":
    main()
