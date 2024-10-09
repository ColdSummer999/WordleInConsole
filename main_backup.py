# Portfolio Project
# name : Matias Tjandradjaja
# student id : J153586

"""
Wordle in Console
__________________

Implementation of a wordle game that can be played on the terminal.

Guess a 5 letters word generated each round.

❌     : The letter does not exist in the secret word
🔵     : The letter exist in the word but not in the right position.
✅     : The letter exist in the word and in the right position.

Only 6 guesses are allowed on a single round.

Version : A.0.1.0
__________________
"""

import random

# Constant declaration
VERSION = 'v.0.1.0'
NUMBER_OF_GUESSES = 6
NUMBER_OF_LETTERS = 5
TARGET_WORD_FILE = 'target_words.txt'
ALL_WORD_FILE = 'all_words.txt'


def white_box():
    return chr(int("2B1C", 16))


def format_space(word):
    formatted_word = ""
    for letter in word:
        formatted_word += letter + " "

    return formatted_word.upper()


def welcome_msg():
    print("___________________________\n"
          + "|     Wordle In Console" "   |\n"
          + "|                         |\n"
          + "| Matias Tjandradjaja     |\n"
          + "| " + str(VERSION) + "                 |\n"
          + "|_________________________|\n")

    print("commands: -help\n")
    return


def mark_guess(secret_word, guess):
    """
    Mark each letters in the secret word using symbols to represent the score

    Args:
        secret_word: The secret word to check
        guess: The player's guess

    :return:
        marking : a list that contains symbols that is populated based on the marked letters
        return marking / scores in symbols format. (e.g.❌🔵✅ )
    """
    marking = []
    # @TODO: Update scoring so when there are multiple letters, only mark found as many times as the
    # @number of the letters

    X_MARK = u'\u274C'
    CIRCLE = u'\U0001F535'
    CHECK_MARK = u'\u2705'

    for letter in range(len(secret_word)):
        # If same letter at the same position
        if secret_word[letter] == guess[letter]:
            marking.append(CHECK_MARK)
        elif guess[letter] in secret_word:
            # If letter not at the same position but exist in the secret word
            marking.append(CIRCLE)
        else:
            # If letter is not found in the secret word
            marking.append(X_MARK)
    return marking


def show_lists(list_of_guess, secret_word, counter_guesses):
    # Show all the entries in the guess list
    for counter in range(len(list_of_guess)):
        if counter < counter_guesses:
            # Only show marking on attempted guess
            marking = mark_guess(secret_word, list_of_guess[counter])
            row_temp = str(counter + 1) + " | "
            for letter in range(len(list_of_guess[counter])):
                row_temp += marking[letter] + list_of_guess[counter][letter].upper() + " "
            print(row_temp)
        else:
            print(str(counter + 1) + " | " + str(list_of_guess[counter]))
    print("")


def initialize_guesses():
    # Initialize empty guesses
    guess_list = []
    guess_content = []

    # Add white boxes to the list as much as the number of letters in a guess
    for x in range(NUMBER_OF_LETTERS):
        guess_content.append(white_box())

    # Paste the created white boxes above as many times as the number of guesses
    for i in range(NUMBER_OF_GUESSES):
        guess_list.append(guess_content)

    return guess_list


def prompt_guess(word_dictionary):
    # Display prompt
    X_MARK = u'\u274C'
    CIRCLE = u'\U0001F535'
    CHECK_MARK = u'\u2705'

    guess = input("-----------------------\n"
                  + X_MARK + ": letter is not in the secret word.\n"
                  + CIRCLE + ": letter is in the secret word but not at the correct position.\n"
                  + CHECK_MARK + ": letter is in the secret word and at the correct position.\n"
                  + "Enter your guess: \n").lower()

    # Process guess and return the input validity
    if guess == "-help":
        print('Guess a 5 letters word and press "enter" to see \n'
              + 'if any of the letter is in the secret word.\n')
        return 'invalid'
    elif guess in word_dictionary and len(guess) == NUMBER_OF_LETTERS:
        return guess
    elif len(guess) != NUMBER_OF_LETTERS:
        print('Please enter a 5 letter word.\n')
        return 'invalid'
    else:
        print('Please enter a valid English word.\n')
        return 'invalid'


def grab_words_from_text(in_file_path):
    # Pick a random word from a text file

    words = []

    file_handle = open(in_file_path, 'r')
    for word in file_handle:
        words.append(word.strip())

    file_handle.close()

    return words


def round_over(secret_word, is_winning):

    if is_winning:
        print("Congratulations! \n"
              + "You have guessed the secret word : " + format_space(secret_word))
    else:
        print("You have reached the number of allowed guesses.")

    prompt_restart = input("\nWould you like to play again? (y/n) : ")
    print()
    while prompt_restart.lower() != 'y' and prompt_restart.lower() != 'n':
        prompt_restart = input("Please enter y or n: ")
    if prompt_restart.lower() == 'y':
        return True
    else:
        print("Thank you for playing, hope to see you again.")
        return False


def play_game():

    playing_game = True

    while playing_game:
        list_of_guess = initialize_guesses()
        playing_round = True
        counter_guesses = 0
        secret_word = random.choice(grab_words_from_text(TARGET_WORD_FILE))
        word_dictionary = grab_words_from_text(ALL_WORD_FILE)
        print(secret_word)
        while playing_round:

            # Show guess chart
            show_lists(list_of_guess, secret_word, counter_guesses)

            # Check if player reached guess limit
            if counter_guesses >= NUMBER_OF_GUESSES:
                if round_over(secret_word, False):
                    playing_game = True
                else:
                    playing_game = False
                break

            guess = prompt_guess(word_dictionary)
            if guess == 'invalid':
                continue
            else:
                for index in range(counter_guesses + 1):
                    list_of_guess[counter_guesses] = guess.lower()
                counter_guesses += 1
                if guess == secret_word:
                    show_lists(list_of_guess, secret_word, counter_guesses)
                    if round_over(secret_word, True):
                        playing_round = False
                    else:
                        playing_round = False
                        playing_game = False


if __name__ == "__main__":
    welcome_msg()
    play_game()
