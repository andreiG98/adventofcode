import os
import heapq
import operator

from tqdm import tqdm

OPERATOR_MAPPER = {
    '+': operator.add, 
    '*': operator.mul
}

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def play_round(instructions, monkeys_inspected_items, active_monkeys, monkey_instructions_len, worry_level_division):
    for idx in range(0, len(instructions), monkey_instructions_len):
        monkey_number = instructions[idx].split(" ")[1].replace(":", "")
        operation_line = instructions[idx + 2].split("=")[-1].strip().split(" ")
        operator = OPERATOR_MAPPER[operation_line[1]]
        
        test = int(instructions[idx + 3].split(" ")[-1])
        true_to_monkey = instructions[idx + 4].split(" ")[-1]
        false_to_monkey = instructions[idx + 5].split(" ")[-1]        
        
        while monkeys_inspected_items[monkey_number]:
            old = monkeys_inspected_items[monkey_number].pop(0)
            first_number = old if operation_line[0] == 'old' else int(operation_line[0])
            second_number = old if operation_line[2] == 'old' else int(operation_line[2])
            
            active_monkeys[monkey_number] += 1
            new = operator(first_number, second_number)
                            
            new //= worry_level_division
                            
            if new % test == 0:
                monkeys_inspected_items[true_to_monkey].append(new)
            else:
                monkeys_inspected_items[false_to_monkey].append(new)


def monkey_business(instructions, rounds=20, top_most_active=2, worry_level_division=3):
    monkey_instructions_len = 7
    monkeys_inspected_items = dict()
    active_monkeys = dict()
    
    for idx in range(0, len(instructions), monkey_instructions_len):
        monkey_number = instructions[idx].split(" ")[1].replace(":", "")
        items = instructions[idx + 1].split(":")[-1].split(",")
        items = list(map(int, items))
        monkeys_inspected_items[monkey_number] = items
        active_monkeys[monkey_number] = 0
        
    for _ in tqdm(range(rounds)):
        play_round(instructions=instructions, monkeys_inspected_items=monkeys_inspected_items, active_monkeys=active_monkeys, 
                    monkey_instructions_len=monkey_instructions_len, worry_level_division=worry_level_division)
            
    print(monkeys_inspected_items)
    print(active_monkeys)
    
    top_n_monkeys = heapq.nlargest(top_most_active, active_monkeys.keys(), key=lambda k: active_monkeys[k])
    monkey_business_sum = 1
    for idx in range(top_most_active):
        monkey_business_sum *= active_monkeys[top_n_monkeys[idx]]

    print(monkey_business_sum)
    

def main():
    file_path = os.path.join(os.getcwd(), 'input2.txt')
    lines = read_file(file_path=file_path)

    monkey_business(lines)
    monkey_business(lines, worry_level_division=1, rounds=1000)

if __name__ == '__main__':
    main()