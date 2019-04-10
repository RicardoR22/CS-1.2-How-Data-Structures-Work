import random
import sys


# Choose the random words to populate the random_words list
def choose_random_words(number_of_words, words_list):
    # Create a list to hold the randomly selected words
    random_words = []

    for num in range(number_of_words):
        # random_words.append(random.choice(words_list).rstrip())
        rand_index = random.randint(0, len(words_list) - 1)
        selected_word = words_list[rand_index].rstrip()
        random_words.append(selected_word)
        
    sentence = ' '.join(random_words)
    print(sentence)

if __name__ == '__main__':
    # Read the words file and create a words list from it
    f = open('/usr/share/dict/words', 'r')
    words_list = f.readlines()
    f.close()

    choose_random_words(int(sys.argv[1]), words_list)
