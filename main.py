import random


def get_random_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    words = contents.split()

    return random.choice(words)


file_path = './five-letters/five_letter_words.txt'
random_word = get_random_word(file_path)
print(random_word)

def game_loop(): # TODO: Implement game loop
    pass