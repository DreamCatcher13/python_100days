import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
    ======''', '''
    +---+
    O   |
        |
        |
    ======''', '''
    +---+
    O   |
    |   |
        |
    ======''', '''
    +---+
    O   |
   /|   |
        |
    ======''', '''
    +---+
    O   |
   /|\  |
        |
    ======''', '''
    +---+
    O   |
   /|\  |
   /    |
    ======''', '''
    +---+
    O   |
   /|\  |
   / \  |
    ======''']

words = []
with open("wordlist.txt", "r") as f:
    words = [line.rstrip() for line in f]

word = words[random.randint(0, len(words)-1)]
print(f"Welcome to Hangman.\n{HANGMAN_PICS[0]}\n"+"_ "*10)
letter_count = len(word)
life_count = 6

display = []
for i in range(letter_count):
    display += "_"
tried_letters = []

while "_" in display:
    guess = input("Your letter: ").lower()
    if guess in tried_letters:
        print(f"* You already guessed {guess}.\n{' '.join(display)}")
        continue
    else:
        tried_letters += guess
    for position in range(len(word)):
        if word[position] == guess:
            display[position] = guess
    if guess not in word:
        print(f"* You guessed {guess}, that's not in the word. You lose a life.")
        print(HANGMAN_PICS[-life_count])
        life_count -= 1
        if life_count == 0: 
            print(f"You lose. The word is {word}")
            break
    print(f"{' '.join(display)}")

if ''.join(display) == word:
    print(f"You won.")
