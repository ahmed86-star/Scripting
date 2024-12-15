# FILE: 2252_AAHMED_LAB07_WorldSeriesAnalyzer.py
# NAME: World Series Winner Analyzer
# AUTHOR(s): ABDIRAHMAN AHMED
# DATE: 11/26/2024
# PURPOSE: To analyze World Series winners and return the number of times a team won, 
#          and the years they won based on user input.

def load_world_series_data(filename):
    """Reads the World Series winners from a file and returns a list of tuples with (team_name, year)."""
    world_series_data = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2): 
                team = lines[i].strip()
                year = lines[i + 1].strip()
                world_series_data.append((team, year))
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error: {e}")
    return world_series_data

def get_team_wins(team, world_series_data):
    """Returns the number of times a team won and the years they won."""
    wins = [year for team_name, year in world_series_data if team_name.lower() == team.lower()]
    return len(wins), wins

def main():
    print("Welcome to the World Series Winner Analyzer!")

    filename = 'WorldSeriesWinners.txt'
    world_series_data = load_world_series_data(filename)

    while True:
        team = input("Enter the name of a team (or 'exit' to quit): ").strip()
        if team.lower() == 'exit':
            break

        wins_count, years_won = get_team_wins(team, world_series_data)

        if wins_count > 0:
            print(f"The team {team} has won {wins_count} time(s).")
            print("They won in the following years:")
            for year in years_won:
                print(year)
        else:
            print(f"The team {team} has not won any World Series.")

        continue_input = input("Would you like to check another team? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

    print("Thank you for using the World Series Winner Analyzer!")

if __name__ == "__main__":
    main()
