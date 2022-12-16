import os
import re
from typing import List, Optional, Set, Union
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


def read_file(file_path) -> List[str]:
    
    with open(file_path) as file:
        lines = [line.strip() for line in file]
        
    return lines


def parse_input(input: List[str]) -> List[List[Point]]:
    sensors = []

    for line in input:
        coordinates = list(map(int, re.findall(r"=(-?\d+)", line)))
        sensors.append([Point(coordinates[0], coordinates[1]), Point(coordinates[2], coordinates[3])])

    return sensors


def manhattan_distance(p1: Point, p2: Point) -> int:

    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def interval_covering(
    start: int, stop: int, sorted_intervals: List[Point], max_dim: int
) -> int:
    for covering_interval in sorted_intervals:
        if stop >= max_dim:

            return max_dim - (stop + 1)

        if stop + 1 < covering_interval[0]:

            return stop + 1

        if interval_right := covering_interval[1] > stop:
            stop = interval_right

    return -1


def row_inspector(
    sensors: List[List[Point]], row: int, max_dim: Optional[int] = None
) -> Union[int, Set[int]]:
    def sensor_coverage(
        sensor_coord: Point, beacon_coord: Point
    ) -> Set[Point]:
        max_dist = manhattan_distance(sensor_coord, beacon_coord)
        surrounding_coords = set()
        if abs(row - sensor_coord.y) <= max_dist:
            x_dof = max_dist - abs(row - sensor_coord.y)
            if max_dist is None:
                for dx in range(-x_dof, x_dof + 1):
                    surrounding_coords.add((sensor_coord.x + dx))
            else:
                surrounding_coords.add((sensor_coord.x - x_dof, sensor_coord.x + x_dof))

        return surrounding_coords

    total_coverage, known_beacon_locs = set(), set()
    for sensor_coord, beacon_coord in sensors:
        total_coverage |= sensor_coverage(sensor_coord, beacon_coord)
        if beacon_coord.y == row:
            known_beacon_locs.add(beacon_coord.x)

    if max_dim is None:
        return len(total_coverage - known_beacon_locs)
    else:
        return interval_covering(
            -1, -1, sorted(total_coverage, key=lambda t: (t[0], -t[1])), max_dim
        )


def distress_beacon_freq(sensors: List[List[Point]], max_dim: int) -> int:
    for row in range(max_dim + 1):
        if distress_beacon_x := row_inspector(sensors, row, max_dim) >= 0:

            return 4_000_000 * distress_beacon_x + row


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    sensors = parse_input(lines)
    print(sensors)

    print(f"part 1: {row_inspector(sensors, 2_000_000)}")
    print(f"part 2: {distress_beacon_freq(sensors, 4_000_000)}")


if __name__ == '__main__':
    main()