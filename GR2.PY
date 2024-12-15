# FILE: 2252_AhmedAbdirahman_Lesson02_CiderMeasurement.py
# NAME: Apple Cider Measurement Calculator & color mixing programS
# AUTHOR(s): Abdirahman Ahmed
# DATE: 9/22/2024


ounces = float(input("Enter the number of ounces of apple cider you want to purchase: "))

drams = ounces * 8  # Convert ounces to drams
gills = ounces / 4   # Convert ounces to gills

print("\nYou have:")
print(f"{gills:.2f} gills")
print(f"{drams:.2f} drams")

if drams > 1024:
    print("That's a large amount! You will need to purchase your cider in gallons.")
elif drams < 100:
    print("That amount is too small. Perhaps you should just order a pint.")



    #Activity 2: Color Mixing Program


    # This program prompts the user to enter two primary colors and mixes them to create a secondary color.

    color1 = input("Enter the first primary color (red, blue, yellow): ").lower()
    color2 = input("Enter the second primary color (red, blue, yellow): ").lower()

    if color1 not in ["red", "blue", "yellow"] or color2 not in ["red", "blue", "yellow"]:
        print("Error: Please enter valid primary colors (red, blue, yellow).")
    elif color1 == color2:
        print("Error: You entered the same color twice. Please enter two different primary colors.")
    else:
        if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
            secondary_color = "purple"
        elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
            secondary_color = "green"
        elif (color1 == "yellow" and color2 == "red") or (color1 == "red" and color2 == "yellow"):
            secondary_color = "orange"

        print(f"The mixture of {color1} and {color2} produces {secondary_color}.")

