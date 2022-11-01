import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Chceck answer against guess, Returns the number of turns left."""
    if guess < answer:
        print("Too low.")
        return turns -1
    elif guess > answer:
        print("Too high.")
        return turns -1
    else:
        print(f"You got it, the answer was {answer}")


def set_dificulity():
    """Function to setting difficulity."""
    level = input("Choose a dificulity 'easy' or 'hard'.").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number guessing game.")
    print("Im thinking of numer between 1 and 100")
    answer = random.randint(1, 100)

    turns = set_dificulity()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps remaining to guess a number.")

        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You are out of turns.")
            return
        elif guess != answer:
            print("Guess again.")

game()