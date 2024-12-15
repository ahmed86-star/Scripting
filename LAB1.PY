#FILE :2252_AhmedAbdirahman_Lesson01_individual_Lab.py
#NAME:  baking brownies!.py
#AUTHOR (s) :  Abdirahman Ahmed
#DAte: 9/7/2024

print("Hi! Let's adjust the brownie recipe based on how many brownies you want to bake.")
print("The original recipe is for 9 brownies.\n")

desired_brownies = int(input("How many brownies do you want to bake? "))

base_brownies = 9
factor = desired_brownies / base_brownies
butter = 0.5 * factor
eggs = 2 * factor
vanilla = 1 * factor
sugar = 1 * factor
flour = 0.5 * factor
cocoa_powder = 0.5 * factor
baking_powder = 0.25 * factor
salt = 0.25 * factor

print("\nHere’s your adjusted recipe for", desired_brownies, "brownies:\n")
print(butter, "cups butter")
print(eggs, "eggs")
print(vanilla, "teaspoons vanilla")
print(sugar, "cups sugar")
print(flour, "cups flour")
print(cocoa_powder, "cups cocoa powder")
print(baking_powder, "teaspoons baking powder")
print(salt, "teaspoons salt")

print("\nEnjoy your brownies!")
