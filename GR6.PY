# FILE: 2252_AhmedAbdirahman_Lesson06.py
# NAME: Random Numbers Analyzer
# AUTHOR(s): Abdirahman Ahmed
# DATE: 11/16/2024

import random

def main():
    print("Welcome to the Random Numbers Analyzer!")

    # Get a valid number of random integers from the user
    while True:
        try:
            num = int(input("Enter the number of random integers to generate: "))
            if num > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("That's not a valid number. Please try again.")
    
    # Generate the random integers
    random_numbers = [random.randint(0, 50) for _ in range(num)]
    
    # Calculate required values
    lowest = min(random_numbers)
    highest = max(random_numbers)
    total_sum = sum(random_numbers)
    average = total_sum / num

    # Display results
    print("\nGenerated List of Random Numbers:", random_numbers)
    print("Lowest Number:", lowest)
    print("Highest Number:", highest)
    print("Total Sum:", total_sum)
    print("Average:", average)

if __name__ == "__main__":
    main()
