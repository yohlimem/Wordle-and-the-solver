import get_random_word
from get_random_word import get_random

word = get_random_word.get_random()

i=0
print(word)
while i<6:
    word_try = input("enter word:   ")
    if(len(word_try)!=5 or word_try not in get_random_word.contents):
        print("please enter a real 5 letter word")
        continue
    char_list = [*word_try]
    output = ""
    for n in range(5):
        if([*word][n]==char_list[n]):
            output +=" right,"
        elif(char_list[n] in [*word]):
            output += " half,"
        else:
            output += " wrong,"

    if(output == " right, right, right, right, right,"):
        print("you won!")
        break

    print(output)
    i+=1
print("womp womp")