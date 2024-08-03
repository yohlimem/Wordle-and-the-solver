import get_random_word
from get_random_word import get_random

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

        if (answer ==[1,1,1,1,1]):
            print("you won!")
            break


        i += 1
        return answer



def guesser():
    for i in range(6):
        word_guess = get_random()
        print(word_guess)
        print(guess(word_guess))
guesser()