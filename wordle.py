import contents
import get_random_word
from get_random_word import get_random
import re

word = get_random_word.get_random()
print(word)
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


def match(word, pattern, wrong_pos,notatall):
    if len(pattern) > len(word):
        return False

    if not all(word[pos] == c for (c, pos) in pattern):
        return False


    if wrong_pos:
        if any(word[pos] == c for (c, pos) in wrong_pos):
            return False
        if all(word[pos] == c for (c, pos) in wrong_pos):
            return False


    if any(c in word for c in notatall):
        return False
    return True


def list_matches(pattern, dictionary, wrong_pos,notattall):
    matches = []
    for word in dictionary:
        if match(word, pattern, wrong_pos,notattall):
            matches.append(word)
            return matches[0]


def guesser():
    word_guess = "אלוהי"
    wrong_pos = []
    notattall=[]
    for i in range(5):


        print(word_guess)
        guessans = (guess(word_guess))
        print(guessans)
        pattern = []
        dictionary = contents.words

        for n in range(5):
            if(guessans[n]==1):
                pattern.append(([*word_guess][n],n))
            elif(guessans[n]==0):
                wrong_pos.append(([*word_guess][n],n))
            else:
                notattall.append([*word_guess][n])

        if(pattern!=[] or wrong_pos!=[]):
            words =list_matches(pattern, dictionary,wrong_pos,notattall)
        else:
            print("random")
            words=get_random_word.get_random()
        if(words==None):
            print("random")
            words=get_random_word.get_random()
        word_guess=words



if __name__ == "__main__":
   guesser()

