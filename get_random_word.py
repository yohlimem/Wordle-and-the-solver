import random

file_path = './five-letters/five_letter_words.txt'
contents = ''
with open(file_path, 'r', encoding='utf-8') as file:
    contents = file.read()

def get_random():

    words = contents.split()

    return random.choice(words)


