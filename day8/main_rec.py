import os

import sys
print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def is_on_edge(i ,j, forest_size):
    if i == 0 or i == forest_size - 1 or j == 0 or j == forest_size - 1:
        return True

    return False


def is_outside(i, j, forest_size):
    if i < 0 or i >= forest_size or j < 0 or j >= forest_size:
        return True

    return False


def traverse_forest(current_point, forest, is_visible_matrix, is_marked_matrix):
    print('current_point')
    print(current_point)
    if is_outside(current_point[0], current_point[1], len(forest)) or is_marked_matrix[current_point[0]][current_point[1]]:
        print('return')
        return

    neighbours_pos = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for neighbour in neighbours_pos:
        next_point = (current_point[0] + neighbour[0], current_point[1] + neighbour[1])

        print('next_point')
        print(next_point)

        is_marked_matrix[current_point[0]][current_point[1]] = True

        if not is_outside(next_point[0], next_point[1], len(forest)) and \
            forest[current_point[0]][current_point[1]] > forest[next_point[0]][next_point[1]] and \
                is_visible_matrix[next_point[0]][next_point[1]]:
            print('da')
            is_visible_matrix[current_point[0]][current_point[1]] = True

        traverse_forest(next_point, forest, is_visible_matrix, is_marked_matrix)


def visible_trees(forest):
    is_visible_matrix = [ [False for _ in range(len(forest))] for _ in range(len(forest))]
    is_marked_matrix = [ [False for _ in range(len(forest))] for _ in range(len(forest))]

    for row_idx, row in enumerate(forest):
        for tree_idx, tree in enumerate(row):

            if is_on_edge(row_idx, tree_idx, len(forest)):
                is_visible_matrix[row_idx][tree_idx] = True

    start_point = (0, 0)

    traverse_forest(start_point, forest, is_visible_matrix, is_marked_matrix)

    print(is_visible_matrix)

    total_tree = 0
    for row in is_visible_matrix:
        total_tree += sum(row)
    print(total_tree)


def main():
    file_path = os.path.join(os.getcwd(), 'input2.txt')
    lines = read_file(file_path=file_path)

    visible_trees(lines)

if __name__ == '__main__':
    main()