import random
import sys


# Read the words file and create a words list from it
f = open('/usr/share/dict/words', 'r')
words_list = f.readlines()
f.close()

# Set the number of words we want selected using the argument that gets passed in
number_of_words = int(sys.argv[1])

# Create a list to hold the randomly selected words
random_words = []

# Choose the random words to populate the random_words list
def choose_random_words():
    for num in range(number_of_words):
        rand_index = random.randint(0, len(words_list) - 1)
        random_words.append(words_list[rand_index].rstrip())
    return


if __name__ == '__main__':
    choose_random_words()
    sentence = ' '.join(random_words)
    print(sentence)
