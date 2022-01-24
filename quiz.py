def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for q in questions:
        print("--------------------")
        print(q + "\n")
        for o in options[question_number - 1]:
            print(o)
        print("")

        guess = input("Enter your answer (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(q), guess)
        question_number += 1

    show_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def show_score(correct_guesses, guesses):
    print("---------")
    print("RESULTS")
    print("---------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("\nYour score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (y/n): ").lower()

    if response == "y":
        return True
    else:
        return False


# create dictionary to hold answers and questions


questions = {
    "Who created Python? ": "A",
    "What planet is the hottest? ": "B",
    "What is the capital of Vietnam? ": "A",
    "When did WWII end? ": "A",
    "In the twisted pair wiring standard 568b, which colour comes first? ": "C",
    "If you are 7 years old and your mother is 31 years old, in how many years will your age be half your mother's? ": "A",
    "How long does a honey bee live for on average? ": "B",
}

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Jeffrey Epstein"],
           ["A. Mercury", "B. Venus", "C. Mars", "D. Earth"],
           ["A. Bangkok", "B. Beijing", "C. Amsterdam", "D. Angola"],
           ["A. 1945", "B. 1944", "C. 1940", "D. 1947"],
           ["A. Blue", "B. Green", "C. Orange", "D. brown"],
           ["A. 17", "B. 15", "C. 7", "D. 25"],
           ["A. 5", "B. 2", "C. 0.75", "D. 10"]]

new_game()

while play_again():
    new_game()

print("\nThanks for playing!")

