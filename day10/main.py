import os
import numpy as np


def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def signal_strength(instructions):

    X = 1
    no_cycles = 1
    verified_cycles = [x for x in range(20, 221, 40)]

    verified_cycles_dict = dict()

    width = 40

    grid = []
    row_string = ""
    for instruction in instructions:
        line_splitted = instruction.split(" ")

        if no_cycles in verified_cycles and no_cycles not in verified_cycles_dict:
            verified_cycles_dict[no_cycles] = no_cycles * X

        if len(line_splitted) == 1: # noop
            row_string += ".#"[abs((no_cycles - 1) % width - X) < 2]
            if no_cycles % width == 0:
                grid.append(row_string)
                row_string = ""

            no_cycles += 1
        else:
            for _ in range(2):
                if no_cycles in verified_cycles and no_cycles not in verified_cycles_dict:
                    verified_cycles_dict[no_cycles] = no_cycles * X

                row_string += ".#"[abs((no_cycles - 1) % width - X) < 2]
                if no_cycles % width == 0:
                    grid.append(row_string)
                    row_string = ""

                no_cycles += 1
                
            _, value = line_splitted

            X += int(value)
        
    print(verified_cycles_dict)
    print(sum(verified_cycles_dict.values()))

    for row in grid:
        print(row)



def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    signal_strength(lines)

if __name__ == '__main__':
    main()