# terminal game of hangman
# (c) 03/2020

from random import randint
from data import hangman, words


print()
print("*" * 17)
print("* H A N G M A N *")
print("*" * 17)

random_word = words[randint(0, len(words) - 1)]
level = 1
old_answer = "-"
bad_tried_letters = ""
letters_tried_twice = []
guessed = []

print("\nThe hidden word has",len(random_word),"characters.")

while level < 13:
    ''' main loop '''

    for pismeno in range(len(random_word)):
        ''' letter counter loop'''

        random_word_list = list(random_word)

        # user input
        answer = input(f"\n [{level}] Guess a letter: ")

        # check for repeated answer
        if answer not in letters_tried_twice:
            letters_tried_twice.append(answer)
        else:
            print("\nYou've guessed this letter in the previous turn already!\n")
            break

        # letter is in the word
        if answer not in random_word:
            print()
            for line in range(len(hangman[level])):
                print(hangman[level][line][0])

            print("\nI'm, sorry, but the word doesn't contain letter", answer.upper(), "! :-(\n")
            bad_tried_letters += answer + ","
            print("Wrong letters already tried:", bad_tried_letters.upper(), "\n")
            level += 1

        # letter is not in the word
        elif answer in random_word:
            print("\nHooray! Letter", answer.upper(), "is there! :-)\n")
            old_answer = answer
            for same_letter_count in range(random_word_list.count(answer)):
                guessed.append(answer)

        # print word pattern
        print("[", end="")
        for letter in random_word:
            if letter in guessed:
                print(letter.upper(), end="")
            else:
                print("-", end="")
        print("]\n")

        # win
        if len(guessed) == len(random_word):
            print("*** YOU WON! ***")
            level = 13
        break

print("\nGAME OVER\n")
