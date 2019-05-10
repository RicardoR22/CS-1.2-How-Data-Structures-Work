from histogram_functions import get_words
import random

def markov_chain(words_list):
    # Key for the chain should be a pair of words in a tuple
    # Values should be a dictionary with the words that follow the pair of words in the tuple
    # along with the amount of times they appear after this pair of words.
    chain = {}
    for index in range(len(words_list) - 1):
        # Set word equal to the word at the current index in words_list
        current_word = word_list[index]
        # Check if word is in the chain
        if current_word in chain:
            word = chain[current_word]
            next_word = word_list[index + 1]
            # Check if the next word in list is in the current words dictionary
            if next_word in word:
                # add 1 to its count if it is
                word[next_word] += 1
            else:
                # otherwise add it to the current words dictuinary with a value of 1
                word[next_word] = 1
        # If the word is not in the chain, add it
        else:
            chain[current_word] = {}
            word = chain[current_word]
            next_word = word_list[index + 1]
            # Check if the next word in list is in the current words dictionary
            if next_word in word:
                # add 1 to its count if it is
                word[next_word] += 1
            else:
                # otherwise add it to the current words dictuinary with a value of 1
                word[next_word] = 1
    return chain

def select_next_word(chain, word):
    # Generate a random frequency from one to max_frequency
    word_dict = chain[word]
    max_frequency = max(word_dict.values())
    rand_frequency = random.uniform(0, max_frequency)
    list_from_word = list(word_dict)
    while True:
        # choose a random index to check
        rand_index = random.randint(0, len(word_dict) - 1)
        selected_word = list_from_word[rand_index]
        # check if the selected words frequency is higher or equal to the randomly generated frequency
        # if it is, return the word
        if word_dict[selected_word] >= rand_frequency:
            return selected_word

def form_sentence(chain, starting_word, sentence_length):
    previous_word = starting_word
    selected_words_list = [starting_word]
    for _ in range(sentence_length - 1):
        selected_word = select_next_word(chain, previous_word)
        selected_words_list.append(selected_word)
        previous_word = selected_word
    sentence = ' '.join(selected_words_list)
    return sentence


if __name__ == '__main__':
    word_list = get_words('GoT_text.txt')
    chain = markov_chain(word_list)
    list_from_chain = list(chain)
    random_word = random.choice(list_from_chain)
    print(random_word)
    sentence = form_sentence(chain, random_word, 10)
    print(sentence)
