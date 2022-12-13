import operator
from collections import defaultdict, deque
import copy
from tqdm import tqdm
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
    operation_operator: operator
    operation_number: any
    test: int
    target: tuple[int, int]


OPERATOR_MAPPER = {
    '+': operator.add, 
    '*': operator.mul
}


def parse_input(input) -> list:
    monkeys = []

    monkey_string = [monkey.strip() for monkey in input.split("\n\n")]

    for m in monkey_string:

        name, items, operation, test, if_true, if_false = [
            line.strip() for line in m.split("\n")
        ]
        items = deque([int(item) for item in items.split(":")[-1].split(",")])
        operation = operation.split("=")[-1].strip().split(" ")
        operation_operator = OPERATOR_MAPPER[operation[1]]
        operation_number = operation[2]
        test = int(test.split(" ")[-1])
        true_to_monkey = int(if_true.split(" ")[-1])
        false_to_monkey = int(if_false.split(" ")[-1])
        target = (true_to_monkey, false_to_monkey)

        monkeys.append(Monkey(items, operation_operator, operation_number, test, target))

    return monkeys


def solve(monkeys: list[Monkey], part: int, rounds: int) -> int:
    monkeys = copy.deepcopy(monkeys)

    divisor = 1
    for m in monkeys:
        divisor *= m.test

    counter = defaultdict(int)
    for _ in tqdm(range(rounds)):
        for i, m in enumerate(monkeys):
            while m.items:
                counter[i] += 1

                old = m.items.popleft()
                # new = eval(m.operation)
                operation_number = old if m.operation_number == 'old' else int(m.operation_number)
                new = m.operation_operator(old, operation_number)

                if part == 1:
                    new //= 3
                else:
                    new %= divisor

                if new % m.test == 0:
                    monkeys[m.target[0]].items.append(new)
                else:
                    monkeys[m.target[1]].items.append(new)


    top, second = sorted(counter.values(), reverse=True)[:2]

    return top * second
    

def main():
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        monkeys_string = puzzle_input.read()

    monkeys = parse_input(monkeys_string)

    print(monkeys)

    part_1_ans = solve(monkeys, part=1, rounds=20)
    print(part_1_ans)

    part_2_ans = solve(monkeys, part=2, rounds=10_000)
    print(part_2_ans)

if __name__ == '__main__':
    main()