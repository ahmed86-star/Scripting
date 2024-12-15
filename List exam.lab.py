# Lists
names = ["Alice", "Bob", "Charlie", "Daisy"]
ages = [25, 30, 35]

# Zip the lists
zipped = list(zip(names, ages))

# Filter pairs where the name has more than 3 characters
filtered = filter(lambda pair: len(pair[0]) > 3, zipped)

# Map to add 5 years to each age in the filtered result
updated_ages = map(lambda pair: (pair[0], pair[1] + 5), filtered)

# Converting to a list for display
result = list(updated_ages)

print("Filtered and Updated Pairs:", result)
# Output: [('Alice', 30), ('Charlie', 40), ('Daisy', 40)]