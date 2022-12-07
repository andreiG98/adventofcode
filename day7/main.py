import os

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def compute_unique_dir_key(dir_stack):

    return '_'.join(dir_stack)


def interpret_command(command, dir_size_dict, dir_stack):
    if command[0] == 'cd': # change directory
        change_dir = command[1]
        if change_dir == '..':
            unique_dir_key_prev = compute_unique_dir_key(dir_stack)

            dir_stack.pop()
            curr_dir = dir_stack[-1]

            unique_dir_key = compute_unique_dir_key(dir_stack)
            if curr_dir != "/":
                # we need to add the size of the chidlren to our parent
                dir_size_dict[unique_dir_key] += dir_size_dict[unique_dir_key_prev]
        else:
            dir_stack.append(change_dir)
    else: # on ls we do not do anything
        pass


def interpret_ls_output(line, dir_size_dict, dir_stack):
    curr_dir = dir_stack[-1]

    unique_dir_key = compute_unique_dir_key(dir_stack)
    if unique_dir_key not in dir_size_dict:
        dir_size_dict[unique_dir_key] = 0

    if line[0] != "dir":
        dir_size_dict[unique_dir_key] += int(line[0])

        if curr_dir != "/":
            dir_size_dict["/"] += int(line[0])


def split_line(line, dir_size_dict, dir_stack):
    line_splitted = line.split(' ')

    if line_splitted[0] == '$': # command
        interpret_command(line_splitted[1:], dir_size_dict, dir_stack)
    else: # ls output
        interpret_ls_output(line_splitted, dir_size_dict, dir_stack)


def find_dirs_aux(console_output, max_size, dir_size_dict, dir_stack):

    if not console_output:
        return

    split_line(console_output[0],dir_size_dict,  dir_stack)

    find_dirs_aux(console_output=console_output[1:], max_size=max_size, dir_size_dict=dir_size_dict, dir_stack=dir_stack)


def find_dirs(console_output, max_size=100000):
    dir_size_dict = dict()
    dir_stack = []

    first_command = console_output[0]
    curr_dir = first_command.split(' ')[-1]

    dir_stack.append(curr_dir)
    
    find_dirs_aux(console_output=console_output[1:], max_size=max_size, dir_size_dict=dir_size_dict, dir_stack=dir_stack)

    print(dir_size_dict)

    filtered_dir_size_dict = { k: v for k, v in dir_size_dict.items() if v <= max_size }

    print(filtered_dir_size_dict)

    print(sum(filtered_dir_size_dict.values()))

    return dir_size_dict


def smallest_to_be_deleted(dir_size_dict, total_space=70000000, space_needed=30000000):
    sorted_dirs = {k: v for k, v in sorted(dir_size_dict.items(), key=lambda item: item[1])}
    free_space = total_space - sorted_dirs["/"]
    space_needed_on_disk = space_needed - free_space
    del sorted_dirs["/"]
    deleted_dirs_dict = dict()
    for k, v in sorted_dirs.items():

        if v >= space_needed_on_disk:
            deleted_dirs_dict[k] = v
            # free_space += v

            break

    print(deleted_dirs_dict)


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    dir_size_dict = find_dirs(lines)

    smallest_to_be_deleted(dir_size_dict)

if __name__ == '__main__':
    main()