#FILE: 2252_AhmedAbdirahman_Lesson03_BrutusDistance.py
# NAME: Brutus Distance Program
# AUTHOR(s): Abdirahman Ahmed
# DATE: 10/5/2024

# This program calculates the distance Brutus the dog runs each hour.
# It uses the formula: distance = speed * time

# Step 1: Get input from the user for how long Brutus played and how fast he ran.
time = int(input("How long did Brutus play fetch? "))
speed = float(input("How fast did Brutus run? "))

# Step 2: Display a header for the table that will show each hour and the corresponding distance
print("\n==========================================")
print("Hour\tBrutus's Distance")
print("==========================================")

# Step 3: Loop through each hour to calculate and display the distance Brutus ran
for hour in range(1, time + 1):
    distance = speed * hour
    print(f"{hour}\t{distance:.2f} km")

    #ACTIVITY 2
    # This program uses nested loops to draw a pattern of hashtags (#).


    # The first half goes from 1 to 6 lines, adding spaces as the line number increases
    for i in range(1, 7):
        print("#" + " " * (i - 1) + "#")

    # The second half goes from 5 to 1 lines, decreasing the number of spaces
    for i in range(5, 0, -1):
        print("#" + " " * (i - 1) + "#")