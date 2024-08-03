import get_random_word

word = get_random_word.get_random()

i=0
while i<6:
    word_try = input("enter word")
    if(len(*word_try)!=5):
        print("please enter a 5 letter word")
        continue

    i+=1