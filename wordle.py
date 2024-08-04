import contents
import get_random_word
import words
from get_random_word import get_random
import re

word = ""
i = 0


def start_game():
    global i
    global word
    i = 0
    word = get_random_word.get_random()
    #word="קלזיו"
    print(word)


def game_loop(word_guess):

    global i
    while i < 6:
        word_try = word_guess
        if len(word_try) != 5 or word_try not in contents.contents:
            print("please enter a real 5 letter word: ", word_try)
            continue
        char_list = [*word_try]
        answer = []
        for n in range(5):
            # if letter is correct make green
            if [*word][n] == char_list[n]:
                answer.append(1)
            # else if letter is in the word make yellow
            elif char_list[n] in [*word]:
                answer.append(0)
            # else make gray
            else:
                answer.append(-1)
        # if all letters are correct
        if answer == [1, 1, 1, 1, 1]:
            print("guessed result: ", word_guess)
            print("you won!")
            return answer

        i += 1
        return answer


def match(word, green_letters, yellow_letters, wrong_letters):
    """word - a word to check
    pattern - a list of tuples (letter, position), green letters, that must appear in the word in the correct place
    wrong_pos - a list of tuples (letter, position), yellow letters, that must appear in the word
    notatall - a list of letters, gray letters, that must not appear in the word
    """

    # if the pattern is longer than the word, it can't be a match
    if len(green_letters) > len(word):
        assert False, f"pattern is longer than word: {green_letters} {word}"
        # return False

    # green letters must appear in the word in the correct place
    if not all(word[pos] == c for (c, pos) in green_letters):
        return False

    # if a letter appears in the same place as the same yellow letter then bad.
    # stops at first wrong letter
    if any(word[pos] == c for (c, pos) in yellow_letters):
        return False

    # yellow letters must appear in the word
    if any(c not in word for (c, pos) in yellow_letters):
        return False

    # gray letters must not appear in the word
    if any(c in word for c in wrong_letters):
        return False

    return True

def get_word_without_used_words(words,words_to_avoid):
    if len(words_to_avoid) > len(words):
        assert False, f"pattern is longer than word: {words_to_avoid} {words}"
    if any(c in word for c in words_to_avoid):
        return False

def list_matches(correct_letters, all_words, yellow_letters, wrong_letters,guess_results,turn):
    # matches = []
    # for word in all_words:
    #     if match(word, pattern, yellow_letters, wrong_letters):
    #         matches.append(word)
    print(guess_results)
    if guess_results.count(1) == 4 and guess_results.count(-1) == 1 and turn<4:
        print("run")

        words_to_avoid = []

        for i, j in correct_letters:
            words_to_avoid.append(i)
        for i, j in yellow_letters:
            words_to_avoid.append(i)
        words_to_avoid+=wrong_letters
        newmatch = filter(lambda word: get_word_without_used_words(all_words, words_to_avoid), all_words)
        print(words_to_avoid)
        new_best_words, best_score = words.best_words(newmatch, words.average_letter_position)
        print(new_best_words)
        if(len(new_best_words)>0):

            print("new word time!")
            return new_best_words[0]

    matches = filter(lambda word: match(word, correct_letters, yellow_letters, wrong_letters), all_words)

    best_words, best_score = words.best_words(matches, words.average_letter_position)
    return best_words[0]


def guesser():
    start_game()
    yellow_letters = []
    wrong_letters = []
    word_guess = "והרלי"

    for i in range(5):
        green_letter = []
        guess_results = game_loop(word_guess)
        if i == 4:
            print("guessed word: ", word_guess)
            print(guess_results)

        dictionary = contents.words
        if guess_results == [1, 1, 1, 1, 1]:
            return True

        if guess_results is None:
            return
        for n in range(5):
            if guess_results[n] == 1:
                green_letter.append(([*word_guess][n], n))
            elif guess_results[n] == 0:
                yellow_letters.append(([*word_guess][n], n))
            else:
                wrong_letters.append([*word_guess][n])

        if len(green_letter) > 0 or len(yellow_letters) > 0 or len(wrong_letters) > 0:
            words = list_matches(
                green_letter, dictionary, yellow_letters, wrong_letters,guess_results,i
            )
        else:

            words = get_random_word.get_random()
        if words is None:
            words = get_random_word.get_random()
        # next word is cool

        word_guess = words

    print("you lost")

    return False


if __name__ == "__main__":
   guesser()
#     correct = 0
#     for i in range(100):
#         if guesser():
#             correct += 1
#         print("=========================================")
#     print(correct / 100)

