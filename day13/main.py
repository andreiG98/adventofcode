import os
from dataclasses import dataclass
import ast
from functools import cmp_to_key


def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.strip() for line in file]
        
    return lines


def parse_input(input):
    pairs: list = []
    for i in range(0, len(input) - 1, 3):
        pair = [ast.literal_eval(input[i]), ast.literal_eval(input[i + 1])]
        pairs.append(pair)

    return pairs


def compare_packets(left, right):

    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]

    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            res = compare_packets(l, r)
        else:
            res = r - l
        
        if res:

            return res

    return len(right) - len(left)


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    pairs = parse_input(lines)

    part1 = sum(idx for idx, (left, right) in enumerate(pairs, 1)
                if compare_packets(left, right) > 0)

    print(f"part 1: {part1}")

    part2 = 1
    sorted_list = sorted([packet for pair in pairs for packet in pair] + [[[2]], [[6]]],
                            key=cmp_to_key(compare_packets), reverse=True)

    for idx, pair in enumerate(sorted_list, 1):
        if pair in ([[2]], [[6]]):
            part2 *= idx

    print(f"part 2: {part2}")

if __name__ == '__main__':
    main()