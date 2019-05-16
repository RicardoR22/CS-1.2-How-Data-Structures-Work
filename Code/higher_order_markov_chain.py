from histogram_functions import get_words
from sampling import higher_markov_check_frequency
import random

def markov_chain(words_list):
    # Key for the chain should be a pair of words in a tuple
    # Values should be a dictionary with the words that follow the pair of words in the tuple
    # along with the amount of times they appear after this pair of words.
    chain = {}
    for index in range(len(words_list) - 2):
        # Set word equal to the word at the current index in words_list
        current_words = (word_list[index], word_list[index + 1])
        next_word = word_list[index + 2]
        # Check if word is in the chain
        if current_words in chain:
            following_words = chain[current_words]
            # Check if the next word in list is in the current words dictionary
            if next_word in following_words:
                # add 1 to its count if it is
                following_words[next_word] += 1
            else:
                # otherwise add it to the current words dictuinary with a value of 1
                following_words[next_word] = 1
        # If the word is not in the chain, add it
        else:
            chain[current_words] = {next_word:1}
    return chain

def select_next_word(chain, starting_words):
    # Generate a random frequency from one to max_frequency
    if starting_words not in chain:
        return

    word_dict = chain[starting_words]
    max_frequency = max(word_dict.values())
    rand_frequency = random.uniform(0, max_frequency)
    list_from_words = list(word_dict)
    while True:
        # choose a random index to check
        rand_index = random.randint(0, len(word_dict) - 1)
        selected_word = list_from_words[rand_index]
        # check if the selected words frequency is higher or equal to the randomly generated frequency
        # if it is, return the word
        if word_dict[selected_word] >= rand_frequency:
            return selected_word

def form_sentence(chain, starting_words, sentence_length):
    previous_words = starting_words
    selected_words_list = [starting_words[0], starting_words[1]]
    for _ in range(sentence_length - 2):
        selected_word = select_next_word(chain, previous_words)
        if selected_word is not None:
            selected_words_list.append(selected_word)
            previous_words = (previous_words[1], selected_word)
    sentence = ' '.join(selected_words_list)
    return sentence


if __name__ == '__main__':
    word_list = get_words('GoT_text.txt')
    chain = markov_chain(word_list)
    list_from_chain = list(chain)
    random_words = random.choice(list_from_chain)
    print(random_words)
    sentence = form_sentence(chain, random_words, 10)
    print(sentence)
    print("sampling info:")
    print(higher_markov_check_frequency(chain))
