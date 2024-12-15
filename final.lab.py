import random

# Header
def show_header():
    print("========================================")
    print("        Welcome to Trivia Game!         ")
    print("========================================\n")

# Function to play the trivia game
def play_game():
    # Questions and answers
    questions = [
        {"question": "How many computer-generated effects were used in the movie Lord of the Rings - Return of the King?",
         "options": ["540", "799", "1205", "1488"],
         "answer": "1488"},
        {"question": "In the movie 'The Blues Brothers', what does Jake order at the diner?",
         "options": ["A medium pizza with pineapple and ham", "3 cheeseburgers with the works and a tall glass of milk",
                     "4 fried chickens and a Coke", "A small Greek salad with extra feta, a steak, 2 baked potatoes, and a coffee"],
         "answer": "4 fried chickens and a Coke"},
        {"question": "In The Simpsons, what football team has Homer always wanted to own?",
         "options": ["Washington Redskins", "Dallas Cowboys", "Denver Broncos", "Cleveland Browns"],
         "answer": "Dallas Cowboys"},
        {"question": "In the TV show Seinfeld, what did Elaine decide was 'her song'?",
         "options": ["I am Woman", "Desperado", "Yesterday", "Witchy Woman"],
         "answer": "Witchy Woman"},
        {"question": "Babe Ruth debuted in professional baseball at the age of 19 years old with which team?",
         "options": ["Boston Red Sox", "New York Yankees", "St Louis Browns", "Cincinnati Reds"],
         "answer": "Boston Red Sox"}
    ]

    random.shuffle(questions)  # Shuffle questions randomly
    correct = 0
    incorrect = 0

    
    for q in questions:
        print(q["question"])
        for idx, option in enumerate(q["options"], start=1):
            print(f"{idx}. {option}")

        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer < 1 or user_answer > len(q["options"]):
                print("Invalid choice! Moving to the next question.\n")
                incorrect += 1
                continue

            if q["options"][user_answer - 1] == q["answer"]:
                print("Correct!\n")
                correct += 1
            else:
                print(f"Wrong! The correct answer is: {q['answer']}\n")
                incorrect += 1
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            incorrect += 1

    print("========================================")
    print(f"Game Over! Your Final Scores:")
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}")
    print("========================================\n")

    return input("Do you want to play again? (yes/no): ").strip().lower() == "yes"


def main():
    show_header()
    while play_game():
        print("\nRestarting the game...\n")

    print("Thanks for playing! Goodbye.")


if __name__ == "__main__":
    main()