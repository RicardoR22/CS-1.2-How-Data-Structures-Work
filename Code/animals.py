from pprint import pprint


def get_words(filename):
    """Open the file and
    return a list of all words in it."""
    all_words_list = []
    with open(filename) as file:
        for line in file:
            words_list = line.split()
            for animal in words_list:
                all_words_list.append(animal)
    return all_words_list

def count_animals(animals_list):
    """Count occurences in the given list of animals_list
    and return that data structure"""
    animal_counts = {}
    for animal_name in animals_list:
        # check if we saw this animal before
        if animal_name in animal_counts:
            # increase its count by 1
            animal_counts[animal_name] += 1
        else:
            # set it's count to 1
            animal_counts[animal_name] = 1

    return animal_counts

def print_table(animal_counts):
    """Prints out a table of animals and their counts."""
    print('Animal | Count')
    print('-----------------')
    for animal_name in animal_counts:
        count = animal_counts[animal_name]
        print('{} | {}'.format(animal_name, count))

animals_list = get_words('animals.txt')
counts = count_animals(animals_list)
pprint(counts)
print_table(counts)
