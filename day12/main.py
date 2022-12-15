import os
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        
        return hash((self.x, self.y))


def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.strip() for line in file]
        
    return lines


def parse_input(input) -> dict[Point, str]:
    # print(input)
    graph = dict()
    for line_idx, line in enumerate(input):
        for col_idx, c in enumerate(line):
            graph[Point(x=col_idx, y=line_idx)] = c

    return graph


def is_possible_move(pos: Point, new_pos: Point, graph: dict[Point, str]):

    return ord(graph[new_pos].replace("E", "z")) - ord(graph[pos].replace("S", "a")) <= 1 if new_pos in graph else False


def adjacents(pos: Point):
    directions = {
        "U": Point(x=0, y=-1),
        "D": Point(x=0, y=1),
        "R": Point(x=1, y=0),
        "L": Point(x=-1, y=0)
    }

    for direction in directions:
        new_x = pos.x + directions[direction].x
        new_y = pos.y + directions[direction].y

        yield Point(x=new_x, y=new_y)


def possible_adjacents(pos: Point, graph: dict[Point, str]):

    return (new_pos for new_pos in adjacents(pos) if is_possible_move(pos, new_pos, graph))


def flood(dist, layers, graph: dict[Point, str]):
    edge = set()

    for pos in layers[-1]:
        for new_pos in possible_adjacents(pos, graph):
            if new_pos not in dist:
                edge.add(new_pos)

    dist.update({ pos: len(layers) for pos in edge })

    if edge:
        flood(dist, layers + [edge], graph)


def distance(start: Point, end: Point, graph: dict[Point, str]):
    dist = {
        start: 0
    }
    flood(dist, [{start}], graph)

    return dist[end] if end in dist else 9999


def find_all(values, graph: dict[Point, str]):
    
    return (pos for (pos, v) in graph.items() if v in values)


def find(value, graph: dict[Point, str]):

    return next(find_all([value], graph))


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    graph: dict[Point, str] = parse_input(lines)
    
    print(f"part1: {distance(find('S', graph), find('E', graph), graph)}")
    print(f"part2: {min(distance(start, find('E', graph), graph) for start in find_all(['a', 'S'], graph))}")


if __name__ == '__main__':
    main()