import random
import sys

words = []
randomized_words = []

def populate_words_list():
    for index in range(1, len(sys.argv)):
        words.append(sys.argv[index])
    return

def rearrange_words():
    for index in range(0, len(words)):
        rand_index = random.randint(0, len(words) - 1)
        randomized_words.append(words[rand_index])
        words.pop(rand_index)
    return

if __name__ == '__main__':
    populate_words_list()
    print(words)
    rearrange_words()
    print(randomized_words)
