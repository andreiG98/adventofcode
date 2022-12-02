import os

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines

def get_most_calories(calories):
        
    most_calories_number = 0
    most_calories_idx = -1
    
    current_calories = 0
    for idx, line in enumerate(calories):
        
        if line != '':
            current_calories += int(line)
        else:
            if current_calories > most_calories_number:
                most_calories_number = current_calories
                most_calories_idx = idx
                
            current_calories = 0
                        
    result_dict = {
        'number_of_calories': most_calories_number,
        'position': most_calories_idx
    }
                
    return result_dict

def get_all_elves_calories(calories):
    all_elves_calories_list = []
    
    current_calories = 0
    for line in calories:
        if line != '':
            current_calories += int(line)
        else:
            all_elves_calories_list.append(current_calories)
            
            current_calories = 0
            
    return all_elves_calories_list

def get_top_three_calories(all_elves_list):
    all_elves_calories_list_sorted = sorted(all_elves_list, reverse=True)
    
    top_three_calories = all_elves_calories_list_sorted[:3]
    
    return top_three_calories

def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)
    
    # part one
    result_dict = get_most_calories(lines)
    print(result_dict)
    
    # part two
    all_elves_calories_list = get_all_elves_calories(lines)
    top_three_calories = get_top_three_calories(all_elves_calories_list)
    print(sum(top_three_calories))

if __name__ == '__main__':
    main()