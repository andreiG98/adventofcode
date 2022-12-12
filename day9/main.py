import os
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


def tail_visited(motions, verbose=False):

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
    if verbose:
        print('initial')
        print(f"head {head}")
        print(f"tail {tail}")

        print()

    visited = set()

    for move in motions:
        direction, amount = move.split()
        amount = int(amount)

        if verbose:
            print(direction, amount)

        for _ in range(amount):
            head.x += directions[direction].x
            head.y += directions[direction].y

            if verbose:
                print(f"head {head}")

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

            if verbose:
                print(f"tail {tail}")
                print("*" * 5)

        if verbose:
            print()

    if verbose:
        print(head)
        print(tail)

    print(len(visited))


def tail_visited_part_two(motions, verbose=False):

    head = Point(x=0, y=0)
    # tail = Point(x=0, y=0)
    tails = [Point(x=0, y=0) for _ in range(9)]

    directions = {
        "U": Point(x=0, y=1),
        "D": Point(x=0, y=-1),
        "R": Point(x=1, y=0),
        "L": Point(x=-1, y=0)
    }
    if verbose:
        print('initial')
        print(f"head {head}")
        print(f"tails {tails}")

        print()

    visited = set()

    for move in motions:
        direction, amount = move.split()
        amount = int(amount)

        if verbose:
            print(direction, amount)

        for _ in range(amount):
            head.x += directions[direction].x
            head.y += directions[direction].y

            if verbose:
                print(f"head {head}")

            for idx_tail in range(len(tails)):
                tail = tails[idx_tail]

                # check if the rope is the first, next to head
                if idx_tail == 0:
                    neighbour = head
                else:
                    neighbour = tails[idx_tail - 1]

                x_diff = neighbour.x - tail.x
                y_diff = neighbour.y - tail.y

                if y_diff == -2:
                    tail.x = neighbour.x
                    tail.y = neighbour.y + 1

                if x_diff == -2:
                    tail.y = neighbour.y
                    tail.x = neighbour.x + 1

                if y_diff == 2:
                    tail.x = neighbour.x
                    tail.y = neighbour.y - 1

                if x_diff == 2:
                    tail.y = neighbour.y
                    tail.x = neighbour.x - 1

                if idx_tail == len(tails) - 1:
                    visited.add((tail.x, tail.y))

                if verbose:
                    print(f"tail {tail}")
                    print("*" * 5)

        if verbose:
            print()

    if verbose:
        print(head)
        print(tails)

    print(len(visited))

def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    tail_visited(lines)
    tail_visited_part_two(lines)

if __name__ == '__main__':
    main()