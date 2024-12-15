# FILE: 2252_AhmedAbdirahman_Lesson06_StateAbbreviations.py
# NAME: State Abbreviation Finder
# AUTHOR(s): Abdirahman Ahmed
# DATE: 11/16/2024

def main():
    print("Welcome to the State Abbreviation Finder!")

    states = {
        "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
        "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
        "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
        "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
        "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
        "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", 
        "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE",
        "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", 
        "New Mexico": "NM", "New York": "NY", "North Carolina": "NC",
        "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
        "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
        "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
        "Vermont": "VT", "Virginia": "VA", "Washington": "WA", 
        "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
    }

    while True:
        print("\nChoose an option:")
        print("1. Find the abbreviation of a state")
        print("2. Find the state name from an abbreviation")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            state_name = input("Enter the full state name: ").title()
            if state_name in states:
                print(f"The abbreviation for {state_name} is {states[state_name]}.")
            else:
                print("State not found. Please check your spelling.")

        elif choice == "2":
            abbreviation = input("Enter the state abbreviation: ").upper()
            state_name = next((state for state, abbrev in states.items() if abbrev == abbreviation), None)
            if state_name:
                print(f"The state with the abbreviation {abbreviation} is {state_name}.")
            else:
                print("Abbreviation not found. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
