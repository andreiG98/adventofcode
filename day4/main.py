import os

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def calculate_elf_interval(elf):
    elf_interval_splitted = elf.split('-')
    elf_interval = set([i for i  in range(int(elf_interval_splitted[0]), int(elf_interval_splitted[1]) + 1)])
    
    return elf_interval


def transform_pair(pair: str):
    first_elf, second_elf = pair.split(',')

    first_elf_interval = calculate_elf_interval(first_elf)
    second_elf_interval = calculate_elf_interval(second_elf)

    return first_elf_interval, second_elf_interval


def check_full_overlap(first_interval, second_interval):

    return first_interval.issubset(second_interval) or second_interval.issubset(first_interval)


def check_overlap(first_interval, second_interval):

    return not first_interval.isdisjoint(second_interval)


def calculate_full_overlapping_pairs(pairs):

    total_overlapping_pairs = 0
    for pair in pairs:

        first_elf_interval, second_elf_interval = transform_pair(pair)

        if check_full_overlap(first_interval=first_elf_interval, second_interval=second_elf_interval):
            total_overlapping_pairs += 1

    return total_overlapping_pairs


def calculate_overlapping_pairs(pairs):

    total_overlapping_pairs = 0
    for pair in pairs:

        first_elf_interval, second_elf_interval = transform_pair(pair)

        if check_overlap(first_interval=first_elf_interval, second_interval=second_elf_interval):
            total_overlapping_pairs += 1

    return total_overlapping_pairs


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    full_overlapping_pairs = calculate_full_overlapping_pairs(lines)
    print(full_overlapping_pairs)

    overlapping_pairs = calculate_overlapping_pairs(lines)
    print(overlapping_pairs)

if __name__ == '__main__':
    main()