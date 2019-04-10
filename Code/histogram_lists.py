from histogram_functions import get_words

def count_words(words_list):
    """Count occurences in the given list of words_list
    and return that data structure"""
    word_counts = []

    for word in words_list:
        # check if we saw this word before
        for list in word_counts:
            # increase its count by 1
            if word in list[0]:
                list[1] += 1
                break
        else:
            # set it's count to 1
            new_list = [word, 1]
            word_counts.append(new_list)


    return word_counts

def print_table(word_counts):
    """Prints out a table of words and their counts."""

    print('Word | Count')
    print('-----------------')
    for list in word_counts:
        count = list[1]
        word = list[0]
        print('{} | {}'.format(word, count))


word_list = get_words('GoT_text.txt')
counts = count_words(word_list)
print_table(counts)
