from histogram_functions import get_words

def count_words(words_list):
    """Count occurences in the given list of words_list
    and return that data structure"""
    word_counts = []

    for word in words_list:
        # check if we saw this word before
        for index, container in enumerate(word_counts):
            # increase its count by 1
            if word in container:
                lst = list(container)
                lst[1] += 1
                word_counts[index] = tuple(lst)
                break
        else:
            # set it's count to 1
            new_tuple = (word, 1)
            word_counts.append(new_tuple)


    return word_counts

def print_table(word_counts):
    """Prints out a table of words and their counts."""

    print('Word | Count')
    print('-----------------')
    for tuple in word_counts:
        count = tuple[1]
        word = tuple[0]
        print('{} | {}'.format(word, count))

if __name__ == '__main__':
    word_list = get_words('GoT_text.txt')
    counts = count_words(word_list)
    print_table(counts)
