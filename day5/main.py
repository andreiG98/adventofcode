import os
import re

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def split_stacks(stacks_lines):
    stacks_dict = {}
    item_step = 4

    for line in stacks_lines:
        splitted_line = line.split(' ')

        idx = 0
        idx_dict = 1

        while idx < len(splitted_line):
            if splitted_line[idx] == '':
                idx += item_step
                idx_dict += 1
            else:
                crate = splitted_line[idx].replace("[", "").replace("]", "")
                if idx_dict not in stacks_dict:
                    stacks_dict[idx_dict] = [crate]
                else:
                    stacks_dict[idx_dict].append(crate)
                
                idx += 1
                idx_dict += 1

    # reverse crates because they are introduced upside down
    for stack_idx in stacks_dict:
        stacks_dict[stack_idx].reverse()

    return stacks_dict


def split_instructions(instructions):
    instructions_list = []
    for instruction in instructions:

        numbers = re.findall(r'\d+', instruction)

        instructions_list.append({
            "amount": int(numbers[0]),
            "from": int(numbers[1]),
            "to": int(numbers[2]),
        })

    return instructions_list


def move_crates(stacks_dict, instructions_list):
    for instruction in instructions_list:
        for _ in range(instruction["amount"]):
            crate = stacks_dict[instruction["from"]].pop()
            stacks_dict[instruction["to"]].append(crate)


def move_multiple_crates(stacks_dict, instructions_list):
    for instruction in instructions_list:

        crates_list = stacks_dict[instruction["from"]][-instruction["amount"]:]
        stacks_dict[instruction["to"]].extend(crates_list)

        for _ in range(instruction["amount"]):
            stacks_dict[instruction["from"]].pop()
        

def top_string(stacks_dict):

    result_top = []
    for stack_idx in range(1, len(stacks_dict) + 1):
        result_top.append(stacks_dict[stack_idx][-1])

    return ''.join(result_top)


def stacks_top(input):
    # we are looking for the line that separate the stacks from the instructions
    idx = 0
    while True:
        if input[idx] == '':
            break

        idx += 1

    stacks_dict = split_stacks(input[:idx - 1])
    instructions_list = split_instructions(input[idx + 1:])

    move_crates(stacks_dict, instructions_list)

    return top_string(stacks_dict)


def stacks_multiple_top(input):
    # we are looking for the line that separate the stacks from the instructions
    idx = 0
    while True:
        if input[idx] == '':
            break

        idx += 1

    stacks_dict = split_stacks(input[:idx - 1])
    instructions_list = split_instructions(input[idx + 1:])

    move_multiple_crates(stacks_dict, instructions_list)

    return top_string(stacks_dict)


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    top = stacks_top(lines)
    print(top)

    multiple_top = stacks_multiple_top(lines)
    print(multiple_top)

if __name__ == '__main__':
    main()