import os
import numpy as np

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def visible_trees(forest):
    grid = []
    for row in forest:
        grid.append([*row])

    grid = np.array(grid)
    visibles = 0
    max_score = float("-inf")

    # traverse the interior
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid)):
            visible = False
            score = 1
            
            curr_tree = grid[row_idx, col_idx]

            # iterate top -> bottom
            for i in range(row_idx + 1, len(grid)):
                if grid[i, col_idx] >= curr_tree:
                    score *= i - row_idx

                    break
            else:
                score *= len(grid) - 1 - row_idx
                visible = True

            # iterate bottom -> top
            for i in range(row_idx - 1, -1, -1):
                if grid[i, col_idx] >= curr_tree:
                    score *= row_idx - i

                    break
            else:
                score *= row_idx
                visible = True

            # iterate left -> right
            for i in range(col_idx + 1, len(grid[0])):
                if grid[row_idx, i] >= curr_tree:
                    score *= i - col_idx

                    break
            else:
                score *= len(grid[0]) - 1 - col_idx
                visible = True

            # iterate right -> left
            for i in range(col_idx - 1, -1, -1):
                if grid[row_idx, i] >= curr_tree:
                    score *= col_idx - i

                    break
            else:
                score *= col_idx
                visible = True

            if visible:
                visibles += 1

            max_score = max(max_score, score)

    print(visibles)
    print(max_score)


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    visible_trees(lines)

if __name__ == '__main__':
    main()