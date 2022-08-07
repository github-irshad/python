import random
from word_list import words
import string
# print(words)

while(True):
    def output_word(words):
        computer_word = random.choice(words)  # choosing random word
        while ' ' in words or '_' in words:
            computer_word = random.choice(words)

        return computer_word

    def hangman():

        valid_word = output_word(words).upper()

        word_letters = set(valid_word)

        alphabets = set(string.ascii_uppercase)

        used_letters = set()
        lives = len(valid_word)

        while len(word_letters) > 0 and lives > 0:

            print(f'you have {lives} lives \n')
            print("you have used these letters : ", ' '.join(used_letters))
            print('\n')

            words_list = [
                letter if letter in used_letters else '_' for letter in valid_word]

            print('current word : ', ' '.join(words_list))
            print('\n')
            user_letter = input("Guess a letter: ").upper()

            if user_letter in alphabets-used_letters:
                used_letters.add(user_letter)
                lives = lives - 1

                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    lives = lives + 1

            elif user_letter in used_letters:
                print("you already entered the letter")
                print('\n')

            else:
                print("Error!")
        print('\n')
        print(valid_word)

    print(hangman())
