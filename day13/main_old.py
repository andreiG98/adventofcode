import os
from dataclasses import dataclass
import ast
from functools import cmp_to_key

@dataclass
class Pair:
    first_packet: list
    second_packet: list


def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.strip() for line in file]
        
    return lines


def parse_input(input):
    pairs: list[Pair] = []
    for i in range(0, len(input) - 1, 3):
        pair = Pair(ast.literal_eval(input[i]), ast.literal_eval(input[i + 1]))
        pairs.append(pair)

    return pairs


def compare_numbers(x, y):
    if x == y:

        return 0

    return 1 if x < y else -1


def compare_packets(pair: Pair):
    print(pair)
    first_packet: list = pair.first_packet
    second_packet: list = pair.second_packet

    idx = 0
    while idx < len(first_packet) and idx < len(second_packet):
        print(idx)
        left_element = first_packet[idx]
        right_element = second_packet[idx]
        ordered = 0

        if isinstance(left_element, int) and isinstance(right_element, int):
            ordered = compare_numbers(left_element, right_element)

        else:
            if isinstance(left_element, int):
                left_element = [left_element]
            if isinstance(right_element, int):
                right_element = [right_element]
            
            ordered = compare_packets(Pair(left_element, right_element))

        if ordered:

            return ordered

        idx += 1


    if idx == len(first_packet) and idx == len(second_packet): # both packets ran out of items

        return 1
    
    if idx == len(first_packet): # first packet ran out of items

        return 1

    return -1 # second packet ran out of items


def right_order_pairs(pairs):
    in_order_pairs = []

    for idx, pair in enumerate(pairs, 1):
        is_in_right_order = compare_packets(pair)

        if is_in_right_order == 1:
            in_order_pairs.append(idx)

    return in_order_pairs


def divider_packets_pairs(pairs):
    print(pairs)

    two_indexes = 1
    six_indexes = 2
    for pair in pairs:
        print(pair)
        first_packet_is_in_right_order = compare_packets(Pair(first_packet=pair.first_packet, second_packet=[[2]])) == 1
        second_packet_is_in_right_order = compare_packets(Pair(first_packet=pair.second_packet, second_packet=[[2]])) == 1

        print(f"first_packet_is_in_right_order {first_packet_is_in_right_order}")
        print(f"second_packet_is_in_right_order {second_packet_is_in_right_order}")

        if first_packet_is_in_right_order == 1:
            two_indexes += 1
        if second_packet_is_in_right_order == 1:
            two_indexes += 1

        first_packet_is_in_right_order = compare_packets(Pair(first_packet=pair.first_packet, second_packet=[[6]])) == 1
        second_packet_is_in_right_order = compare_packets(Pair(first_packet=pair.second_packet, second_packet=[[6]])) == 1

        print(f"first_packet_is_in_right_order {first_packet_is_in_right_order}")
        print(f"second_packet_is_in_right_order {second_packet_is_in_right_order}")

        if first_packet_is_in_right_order == 1:
            six_indexes += 1
        if second_packet_is_in_right_order == 1:
            six_indexes += 1


    decoder_key = two_indexes * six_indexes

    return decoder_key


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    pairs = parse_input(lines)

    in_order_pairs = right_order_pairs(pairs)

    print(f"part 1: {sum(in_order_pairs)}")

    print('*' * 20)
    decoder_key = divider_packets_pairs(pairs)

    print(f"part 2: {decoder_key}")

if __name__ == '__main__':
    main()