from histogram_functions import get_words

def count_words(words_list):
    """Count occurences in the given list of words_list
    and return that data structure"""
    word_counts = {}
    for word in words_list:
        # check if we saw this word before
        if word in word_counts:
            # increase its count by 1
            word_counts[word] += 1
        else:
            # set it's count to 1
            word_counts[word] = 1

    return word_counts



word_list = get_words('GoT_text.txt')
counts = count_words(word_list)
print_table(counts)
