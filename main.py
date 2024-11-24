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


def score_guess(secret_word, guess):
    """
    Mark each letters in the secret word using symbols to represent the score

    Args:
        secret_word: The secret word to check
        guess: The player's guess
    Params:
        0 : Letter not found in the secret word.
        1 : Letter found but not in the correct position.
        2 : Letter is in the correct position
    :return:
        marking : a list that contains symbols that is populated based on the marked letters
        return  scores in numerical format. (e.g. 0, 1, 2 )
    """
    scores = ()
    # @TODO: Update scoring so when there are multiple letters, only mark found as many times as the
    # @number of the letters
    x_mark = u'\u274C'
    circle = u'\U0001F535'
    check_mark = u'\u2705'

    letter_count = {}
    for letter in range(len(secret_word)):
        letter_count[secret_word[letter]] = secret_word.count(secret_word[letter])

    letter_found = {}
    for letter in range(len(secret_word)):
        letter_found[secret_word[letter]] = 1

    for letter in range(len(secret_word)):
        # If same letter at the same position
        if secret_word[letter] == guess[letter]:
            letter_found[secret_word[letter]] = letter_found[secret_word[letter]] + 1
            scores += tuple(str("2"))
        elif guess[letter] in secret_word:
            # If letter not at the same position but exist in the secret word and not more than count
            if letter_found[secret_word[letter]] > letter_count[secret_word[letter]]:
                scores += tuple(str("0"))
            else:
                letter_found[secret_word[letter]] = letter_found[secret_word[letter]] + 1
                if letter_found[secret_word[letter]] > letter_count[secret_word[letter]]:
                    scores += tuple(str("1"))
                else:
                    scores += tuple(str("0"))
        else:
            # If letter is not found in the secret word
            scores += tuple(str("0"))

    return scores


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
    x_mark = u'\u274C'
    circle = u'\U0001F535'
    check_mark = u'\u2705'
    # Add letter to dictionary as key and the value as the number of times the letter appear in the string
    letter_count = {}
    for letter in range(len(secret_word)):
        letter_count[secret_word[letter]] = secret_word.count(secret_word[letter])

    letter_found = {}
    for letter in range(len(secret_word)):
        letter_found[secret_word[letter]] = 1

    for letter in range(len(secret_word)):
        # If same letter at the same position
        if secret_word[letter] == guess[letter]:
            letter_found[secret_word[letter]] = letter_found[secret_word[letter]] + 1
            marking.append(check_mark)
        elif guess[letter] in secret_word:
            # If letter not at the same position but exist in the secret word and not more than count
            if letter_found[secret_word[letter]] > letter_count[secret_word[letter]]:
                marking.append(x_mark)
            else:
                letter_found[secret_word[letter]] = letter_found[secret_word[letter]] + 1
                if letter_found[secret_word[letter]] > letter_count[secret_word[letter]]:
                    marking.append(circle)
                else:
                    marking.append(x_mark)
        else:
            # If letter is not found in the secret word
            marking.append(x_mark)
    return marking


def show_lists(list_of_guess, secret_word, counter_guesses):
    # Show all the entries in the guess list
    for index in range(len(list_of_guess)):
        if index < counter_guesses:
            # Only show marking on attempted guess
            marking = mark_guess(secret_word, list_of_guess[index])
            scores = score_guess(secret_word, list_of_guess[index])
            row_temp = str(index + 1) + " | "
            for letter in range(len(list_of_guess[index])):
                row_temp += marking[letter] + list_of_guess[index][letter].upper() + " "
            print(row_temp)
            row_temp = ""
            for letter in list(scores):
                row_temp += letter + " "
            print(row_temp)
        else:
            print(str(index + 1) + " | " + str(list_of_guess[index]))
    print("")


def initialize_guesses(number_of_guesses, number_of_letters):
    # Initialize empty guesses
    guess_list = []
    guess_content = []

    # Add white boxes to the list as much as the number of letters in a guess
    for letter_index in range(number_of_letters):
        guess_content.append(white_box())

    # Paste the created white boxes above as many times as the number of guesses
    for guess_index in range(number_of_guesses):
        guess_list.append(guess_content)

    return guess_list


def prompt_guess(word_dictionary, number_of_letters):
    # Display prompt
    x_mark = u'\u274C'
    circle = u'\U0001F535'
    check_mark = u'\u2705'
    guess = input("-----------------------\n"
                  + x_mark + ": letter is not in the secret word.\n"
                  + circle + ": letter is in the secret word but not at the correct position.\n"
                  + check_mark + ": letter is in the secret word and at the correct position.\n"
                  + "Enter your guess: \n").lower()

    # Process guess and return the input validity
    if guess == "-help":
        print('Guess a 5 letters word and press "enter" to see \n'
              + 'if any of the letter is in the secret word.\n')
        return 'invalid'
    elif guess in word_dictionary and len(guess) == number_of_letters:
        return guess
    elif len(guess) != number_of_letters:
        print('Please enter a 5 letter word.\n')
        return 'invalid'
    else:
        print('Please enter a valid English word.\n')
        return 'invalid'


def grab_words_from_file(filepath):
    # Read words from file and store them into a list
    words = []

    file_handle = open(filepath, 'r')
    for word in file_handle:
        words.append(word.strip())

    file_handle.close()

    return words


def round_over(secret_word, is_winning, filepath, tries, player_name):

    if is_winning:
        print("Congratulations! \n"
              + "You have guessed the secret word : " + format_space(secret_word))
    else:
        print("Sorry, you have reached the number of allowed guesses.\n"
              + "The secret word is : " + format_space(secret_word))

    # Write statistics
    write_statistics(filepath, player_name, secret_word, tries, is_winning)

    prompt_restart = input("\nWould you like to play again? (y/n) : ")
    print()
    while prompt_restart.lower() != 'y' and prompt_restart.lower() != 'n':
        prompt_restart = input("Please enter y or n: ")
    if prompt_restart.lower() == 'y':
        return True
    else:
        print("Thank you for playing, hope to see you again.")
        return False


def enter_player_name():
    player_name = input("Please enter your name without whitespace \n"
                        + "or leave blank if you wish to remain anonymous.\n"
                        + "Name : ")
    if player_name == "":
        return "anonymous"
    if ' ' in player_name:
        return "invalid"
    else:
        return player_name


def get_statistics(filepath, player_name):
    """
        Read statistics file
            Format :
            Name, Word, Tries, Successful?, Word, Tries, Successful?
    """
    file_handle = open(filepath, "r+")
    statistics = []

    for line in file_handle:
        line = line.strip()
        statistics = line.split(",")
        if '' in statistics:
            statistics.remove('')
        if len(statistics) >= 1:
            if statistics[0] == player_name:
                if len(statistics) >= 2:
                    # Return statistic if there is any stats recorded for the associated player.
                    statistics = line.split(",")
                file_handle.readline()
                file_handle.close()
                return statistics

    # Player not found, add to statistics
    file_handle.readline()
    file_handle.write("\n" + player_name)
    file_handle.close()
    return []


def write_statistics(filepath, player_name, secret_word, tries, is_successful):
    """
        Write statistics to a file
            Format :
            Name, Word, Tries, Successful?, Word, Tries, Successful?
    """
    file_handle = open(filepath, "r+")
    content = file_handle.readlines()
    success = "Successful" if is_successful else "Unsuccessful"
    found_in_index = 0
    old_content = ""
    for line in range(len(content)):
        statistics = content[line].split(",")
        if '' in statistics:
            statistics.remove('')
        if len(statistics) >= 1:
            if statistics[0].strip() == player_name:
                # Found the player, save the index of the line
                found_in_index = line
                old_content += content[line]
                break

    file_handle.close()
    content[found_in_index] = old_content.strip() + "," + secret_word + "," + str(tries) + "," + success + "\n"
    file_handle = open(filepath, "w")
    file_handle.writelines(content)
    file_handle.close()

def display_statistics(statistics):
    print("Name : " + statistics[0])
    counter = 0
    stat = ""
    for index in range(1, len(statistics)):
        if counter == 0:
            stat += "Word : " + statistics[index] + " "
        elif counter == 1:
            stat += "Tries : " + statistics[index] + " "
        else:
            stat += ", " + statistics[index]
        counter += 1
        if counter >= 3:
            counter = 0
            print(stat)
            stat = ""


def play_game():

    debug_cheat = False

    playing_game = True
    number_of_guesses = 6
    number_of_letters = 5
    target_word_file = 'target_words.txt'
    all_words_file = 'all_words.txt'
    statistic_file = 'statistics.txt'
    default_player_name = "anonymous"

    input_player_name = True
    player_name = "anonymous"

    # Statistics
    while input_player_name:
        player_name = enter_player_name()
        if player_name == "invalid":
            print("No white space allowed!")
            continue
        else:
            input_player_name = False

    statistics = []
    try:
        statistics = get_statistics(statistic_file, player_name)
    except FileNotFoundError:
        # If file not found, create one
        file_handle = open(statistic_file, "w")
        file_handle.close()
        statistics = get_statistics(statistic_file, player_name)

    if len(statistics) >= 2:
        # If statistics exist for the player, display it
        print("Welcome back " + player_name + ". Your statistics are:")
        display_statistics(statistics)
    else:
        # Otherwise just welcome the player to the game
        print("Welcome to the game " + player_name + "\n")

    while playing_game:
        list_of_guess = initialize_guesses(number_of_guesses, number_of_letters)
        playing_round = True
        counter_guesses = 0
        secret_word = random.choice(grab_words_from_file(target_word_file))

        word_dictionary = grab_words_from_file(all_words_file)

        while playing_round:
            # Show guess chart
            show_lists(list_of_guess, secret_word, counter_guesses)

            # Check if player reached guess limit
            if counter_guesses >= number_of_guesses:
                if round_over(secret_word, False, statistic_file, counter_guesses, player_name):
                    playing_game = True
                else:
                    playing_game = False
                break

            guess = prompt_guess(word_dictionary, number_of_letters)
            if guess == 'invalid':
                continue
            else:
                for index in range(counter_guesses + 1):
                    list_of_guess[counter_guesses] = guess.lower()
                counter_guesses += 1
                if guess == secret_word:
                    show_lists(list_of_guess, secret_word, counter_guesses)
                    if round_over(secret_word, True, statistic_file, counter_guesses, player_name):
                        playing_round = False
                    else:
                        playing_round = False
                        playing_game = False


if __name__ == "__main__":
    welcome_msg()
    play_game()
