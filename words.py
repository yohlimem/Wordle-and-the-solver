from main import get_random_word
from main import contents

# https://www.sttmedia.com/characterfrequency-hebrew
def get_letter_percentage(letter):
    match letter:
        case "א":
            return 6.34
        case 'ב':
            return 4.74
        case 'ג':
            return 1.30
        case 'ד':
            return 2.59
        case 'ה':
            return 10.87
        case 'ו':
            return 10.38
        case 'ז':
            return 1.33
        case 'ח':
            return 2.48
        case 'ט':
            return 1.24
        case 'י':
            return 11.06
        case 'כ':
            return 2.70
        case 'ל':
            return 7.39
        case 'מ':
            return 4.59
        case 'נ':
            return 2.86
        case 'ס':
            return 1.48
        case 'ע':
            return 3.23
        case 'פ':
            return 1.69
        case 'צ':
            return 1.24
        case 'ק':
            return 2.14
        case 'ר':
            return 5.61
        case 'ש':
            return 4.41
        case 'ת':
            return 5.01
        case 'ך':
            return 0.81
        case 'ם':
            return 3.03
        case 'ן':
            return 1.10
        case 'ף':
            return 0.27
        case 'ץ':
            return 0.12
    return 0.00001

def get_letter_count(word):
    chars = [x for x in word]
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


# we want the word with the most common letters
# we want the word with the most different letters

def get_word_score(word):
    score = 0

    # more of the same letter is bad
    # more common is good

    # normalize the word count
    word_count = get_letter_count(word)
    max_count = max(word_count.values())
    # print(word_count)

    word_count = {k: (v / len(word_count.items())) for k, v in word_count.items()}

    # print(word_count)

    score += sum([v / get_letter_percentage(k) for k, v in word_count.items()])
    return score

def best_words():
    best_score = 100000
    # best_word = ''
    best_words = []
    words = contents.split()
    for word in words:
        score = get_word_score(word)
        if score == 0:
            continue
        if score < best_score:
            best_score = score
            best_words = [word]
            print(f"New best word: {word} with score {score}")
        elif abs(score - best_score) < 0.001:
            best_words.append(word)
        
    return best_words, best_score

if __name__ == "__main__":
    # get_word_score(get_random_word())
    print(best_words())
