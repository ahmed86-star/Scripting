import os

# Define main function
def main():
    # Get current working directory
    current_dir = os.getcwd()

    # List all items in the directory
    items = os.listdir(current_dir)

    # Process each item
    for item in items:
        # Check for log files
        if item.endswith(".log"):
            try:
                # Open the log file and process it
                with open(item, 'r') as file:
                    matches = get_matches(file, "pass")
                    print(f"File: {item}")
                    for line_num, line_content in matches:
                        print(f"Line {line_num}: {line_content.strip()}")
            except Exception as e:
                print(f"Error processing {item}: {e}")

# Function to find lines containing a specific keyword
def get_matches(file, keyword):
    matches = []
    for line_num, line in enumerate(file, start=1):
        if line.startswith(keyword):
            matches.append((line_num, line))
    return matches

if __name__ == "__main__":
    main()