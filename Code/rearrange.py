import random
import sys

# Could use random.shuffle() to shuffle the order of the argument list, but decided to work it out instead.

words = []
randomized_words = []

# This function appends the arguments provided into the words list
def populate_words_list():
    for index in range(1, len(sys.argv)):
        words.append(sys.argv[index])

# This function chooses a random word from the words list,
# then appends it to the randomized_words list, before removing it from the words list
def rearrange_words():
    for index in range(0, len(words)):
        rand_index = random.randint(0, len(words) - 1)
        randomized_words.append(words[rand_index])
        words.pop(rand_index)

if __name__ == '__main__':
    populate_words_list()
    rearrange_words()
    print(' '.join(randomized_words))
