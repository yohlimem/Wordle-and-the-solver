import contents
import get_random_word
from get_random_word import get_random
import re

word = get_random_word.get_random()
print(word)
i = 0


def game_loop(word_guess):
    global i

    while i < 6:
        word_try = word_guess
        if len(word_try) != 5 or word_try not in contents.contents:
            print("please enter a real 5 letter word")
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
            print("you won!")
            return answer

        i += 1
    return answer


def match(word, green_letters, yellow_letters, wrong_letters):
    ''' word - a word to check
        pattern - a list of tuples (letter, position), green letters, that must appear in the word in the correct place
        wrong_pos - a list of tuples (letter, position), yellow letters, that must appear in the word
        notatall - a list of letters, gray letters, that must not appear in the word
    '''
    
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


def list_matches(pattern, all_words, yellow_letters, wrong_letters):
    matches = []
    for word in all_words:
        if match(word, pattern, yellow_letters, wrong_letters):
            matches.append(word)
            return matches[0]


def guesser():
    yellow_letters = []
    wrong_letters = []
    word_guess = "אחיהן"

    for i in range(5):
        green_letter = []

        print(word_guess)
        guess_results = game_loop(word_guess)
        print(guess_results)

        dictionary = contents.words
        if guess_results == None:
            break
        for n in range(5):
            if guess_results[n] == 1:
                green_letter.append(([*word_guess][n], n))
            elif guess_results[n] == 0:
                yellow_letters.append(([*word_guess][n], n))
            else:
                wrong_letters.append([*word_guess][n])

        if len(green_letter) > 0 or len(yellow_letters) > 0 or len(wrong_letters) > 0:
            words = list_matches(green_letter, dictionary, yellow_letters, wrong_letters)
        else:
            print("random")
            words = get_random_word.get_random()
        if words == None:
            print("random")
            words = get_random_word.get_random()
        # next word is cool
        word_guess = words
        print(green_letter)
        print(wrong_letters)
        print(yellow_letters)


if __name__ == "__main__":
    guesser()
