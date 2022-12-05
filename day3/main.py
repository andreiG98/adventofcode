import os

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def split_rucksack(rucksack):
    rucksack_half = int(len(rucksack) / 2)

    return rucksack[:rucksack_half], rucksack[rucksack_half:]


def intersection_sum(*items):

    intersection = set.intersection(*items)

    rucksack_sum = 0
    for letter in intersection:
        # Lowercase item types a through z have priorities 1 through 26.
        # Uppercase item types A through Z have priorities 27 through 52.
        if letter.islower():
            letter_score = ord(letter) - 96
        else:
            letter_score = ord(letter) - 38

        rucksack_sum += letter_score

    return rucksack_sum

    
def calculate_score(rucksacks):
    total_sum = 0

    for rucksack in rucksacks:

        first_compartement, second_compartement = split_rucksack(rucksack=rucksack)

        first_compartement_items = set(first_compartement)
        second_compartement_items = set(second_compartement)

        rucksack_sum = intersection_sum(first_compartement_items, second_compartement_items)

        total_sum += rucksack_sum

    return total_sum


def calculate_score_part_two(rucksacks):
    total_sum = 0

    group_len = 3
    for idx in range(0, len(rucksacks), group_len):

        rucksacks_group = [set(rucksack) for rucksack in rucksacks[idx:idx + group_len]]
        rucksack_sum = intersection_sum(*rucksacks_group)

        total_sum += rucksack_sum

    return total_sum


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)
    
    score = calculate_score(lines)
    print(score)

    score_part_two = calculate_score_part_two(lines)
    print(score_part_two)

if __name__ == '__main__':
    main()