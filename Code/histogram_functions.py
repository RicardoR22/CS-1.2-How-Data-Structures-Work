def get_words(filename):
    """Open the file and
    return a list of all words in it."""
    all_words_list = []
    with open(filename) as file:
        for line in file:
            words_list = line.split()
            for word in words_list:
                # Removes special characters from the end of the word
                word_no_characters = word.translate({ord(c): None for c in '-?!@#$,.'})
                word_no_spaces = word.strip()
                word = word_no_spaces.lower()
                all_words_list.append(word)
    return all_words_list


# def print_table(word_counts):
#     """Prints out a table of words and their counts."""
#     print('Word | Count')
#     print('-----------------')
#     for word in word_counts:
#         count = word_counts[word]
#         print('{} | {}'.format(word, count))
