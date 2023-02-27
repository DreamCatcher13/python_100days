import random


HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']

words = []
with open("wordlist.txt", "r") as f:
    words = [line.rstrip() for line in f]

word = words[random.randint(0, len(words)-1)]
guess = input("your letter ").lower()
for letter in word:
    if letter == guess:
        print(f"Right")
    else:
        print(f"Wrong")

print(word)
