from histogram_functions import get_words
from histogram_lists import count_words
import random

# def sample_by_frequency(histogram):
#     # TODO: select a word based on frequency
#     list_from_histogram = []
#     for item in histogram:
#         for count in range(0, item[1]):
#             list_from_histogram.append(item[0])
#
#     rand_index = random.randint(0, len(list_from_histogram) - 1)
#     return list_from_histogram[rand_index]

def another_sample_by_frequency(histogram):
    # Find the most any word appears and set max_frequency equal to that value
    max_frequency = 0
    for item in histogram:
        if item[1] > max_frequency:
            max_frequency = item[1]

    # Generate a random frequency from one to max_frequency
    rand_frequency = random.randint(0, max_frequency)

    while True:
        # choose a random index to check
        rand_index = random.randint(0, len(histogram) - 1)
        selected_list = histogram[rand_index]
        # check if the selected words frequency is higher or equal to the randomly generated frequency
        # if it is, return the word
        if selected_list[1] >= rand_frequency:
            return selected_list[0]


def check_frequency(histogram):
    frequency_dict = {}
    for _ in range(10000):
        word = another_sample_by_frequency(histogram)
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


if __name__ == '__main__':
    word_list = get_words('GoT_text.txt')
    counts = count_words(word_list)
    #sample = sample_by_frequency(counts)
    sample2 = another_sample_by_frequency(counts)
    frequency_check = check_frequency(counts)
    #print(sample)
    print(sample2)
    print(frequency_check)
