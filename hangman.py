import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Welcome to hangman game.")
print("------------------------")

random_words = ["aardvark", "baboon", "camel"]

#choosing random word from list
word = random.choice(random_words)


display = []
for letter in word:
    display.append("_")


lives = 6
helper = -1
#WHILE NOT WIN KEEP IT DOING
while "_" in display:
    guess = input("Guess the letter: \n").lower()
    #print(stages[-1])

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        helper -= 1
        if lives == 0:
            print("YOU HAVE LOST U PRICK")
            break

        print(stages[helper])


    print(f" ".join(display))


