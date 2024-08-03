import get_random_word
from get_random_word import get_random
import re

word = get_random_word.get_random()
#print(word)
i = 0
def guess(word_guess):
    global i

    while i < 6:
        word_try = word_guess
        if (len(word_try) != 5 or word_try not in get_random_word.contents):
            print("please enter a real 5 letter word")
            continue
        char_list = [*word_try]
        answer = []
        for n in range(5):
            if ([*word][n] == char_list[n]):
                answer.append(1)
            elif (char_list[n] in [*word]):
                answer.append(0)
            else:
                answer.append(-1)
        answer.reverse()
        if (answer ==[1,1,1,1,1]):
            print("you won!")
            break


        i += 1
        return answer



def match(word, pattern):
    if len(pattern) > len(word):
        return False

    return all(word[pos] == c for (c, pos) in pattern)

def list_matches(pattern, dictionary):
    for word in dictionary:
        if match(word, pattern):
            return word


def guesser():
    word_guess = get_random()
    for i in range(6):



        guessans = (guess(word_guess))
        pattern = []
        dictionary = get_random_word.contents

        for n in range(5):
            if(guessans[n]==1):
                pattern.append(([*word_guess][n],n))

        words =list_matches(pattern, dictionary)[0]

        word_guess=words



#if __name__ == "__main__":
   # guesser()


pattern = [("א", 0)]
dictionary =get_random_word.contents

list_matches(pattern, dictionary)

