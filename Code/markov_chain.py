from histogram_functions import get_words

def markov_chain(words_list):
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

word_list = get_words('fish.txt')
chain = markov_chain(word_list)
print(chain)
