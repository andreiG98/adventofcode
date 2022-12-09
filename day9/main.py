import os
import numpy as np
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def is_adjacent(point1: Point, point2: Point):
    x_diff = abs(point1.x - point2.x)
    y_diff = abs(point1.y - point2.y)

    if x_diff == 1 or y_diff == 1:

        return True
    
    return False


def is_diagonally_adjacent(point1: Point, point2: Point):
    x_diff = abs(point1.x - point2.x)
    y_diff = abs(point1.y - point2.y)

    if x_diff == 1 and y_diff == 1:

        return True
    
    return False


def tail_visited(motions):

    # moves_len = [motion.split()[1] for motion in motions]
    # max_len = np.amax(np.array(moves_len, dtype=int))

    # grid = np.zeros((max_len, max_len))

    # print(grid)

    head = Point(x=0, y=0)
    tail = Point(x=0, y=0)

    directions = {
        "U": Point(x=0, y=1),
        "D": Point(x=0, y=-1),
        "R": Point(x=1, y=0),
        "L": Point(x=-1, y=0)
    }
    print('initial')
    print(f"head {head}")
    print(f"tail {tail}")

    print()

    visited = set()

    with open('output_main.txt', "w") as file:
        for move in motions:
            direction, amount = move.split()
            amount = int(amount)

            print(direction, amount)

            for _ in range(amount):
                head.x += directions[direction].x
                head.y += directions[direction].y

                print(f"head {head}")

                # if is_diagonally_adjacent(head, tail):
                x_diff = head.x - tail.x
                y_diff = head.y - tail.y

                if y_diff == -2:
                    tail.x = head.x
                    tail.y = head.y + 1

                if x_diff == -2:
                    tail.y = head.y
                    tail.x = head.x + 1

                if y_diff == 2:
                    tail.x = head.x
                    tail.y = head.y - 1

                if x_diff == 2:
                    tail.y = head.y
                    tail.x = head.x - 1

               

                visited.add((tail.x, tail.y))

                print(f"tail {tail}")
                print("*" * 5)

            print()

        print(head)
        print(tail)

        print(len(visited))


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    tail_visited(lines)

if __name__ == '__main__':
    main()