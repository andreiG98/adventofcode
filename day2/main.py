import os

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def split_input(strategy):
    
    you_choices = []
    opponent_choices = []
    
    for line in strategy:
        opponent, you = line.split(' ')
        
        you_choices.append(you)
        opponent_choices.append(opponent)
        
    return {
        'you': you_choices,
        'opponent': opponent_choices
    }
    
def calculate_score(strategy_dict):
    
    shape_score_dict = {
        'X': 1, # Rock
        'Y': 2, # Paper
        'Z': 3, # Scissors
    }
    round_score_dict = {
        'lost': 0,
        'draw': 3,
        'won': 6,
    }
    
    opponent_choice_dict = {
        'A': 1, # Rock
        'B': 2, # Paper
        'C': 3, # Scissors
    }
    you_choice_dict = {
        'X': 1, # Rock
        'Y': 2, # Paper
        'Z': 3, # Scissors
    }
    
    total_score = 0
    
    you_choices, opponent_choices = strategy_dict['you'], strategy_dict['opponent']
    
    for you_choice, opponent_choice in zip(you_choices, opponent_choices):
        
        you_choice_number = you_choice_dict[you_choice]
        opponent_choice_number = opponent_choice_dict[opponent_choice]
                
        total_score += shape_score_dict[you_choice]
        # trivial case, draw
        if you_choice_number == opponent_choice_number:
            total_score += round_score_dict['draw']
        # paper > rock, scissors > paper
        elif abs(you_choice_number - opponent_choice_number) == 1:
            if you_choice_number > opponent_choice_number:
                total_score += round_score_dict['won']
            else:
                total_score += round_score_dict['lost']
        # rock > scissors
        else:
            if you_choice_number < opponent_choice_number:
                total_score += round_score_dict['won']
            else:
                total_score += round_score_dict['lost']
        
    return total_score
    
def calculate_score_part_two(strategy_dict):
    """"
    X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    """
    
    outcome_score_dict = {
        'X': 0, # lose
        'Y': 3, # draw
        'Z': 6, # win
    }
    
    opponent_choice_dict = {
        'A': 1, # Rock
        'B': 2, # Paper
        'C': 3, # Scissors
    }
    
    total_score = 0
    
    you_choices, opponent_choices = strategy_dict['you'], strategy_dict['opponent']
    
    for you_choice, opponent_choice in zip(you_choices, opponent_choices):
                
        total_score += outcome_score_dict[you_choice]
        
        # trivial case, draw
        if you_choice == 'Y':
            total_score += opponent_choice_dict[opponent_choice]
        # lose
        elif you_choice == 'X':
            new_choice = opponent_choice_dict[opponent_choice] - 1
            if new_choice == 0:
                new_choice = 3
            total_score += new_choice
        # win
        else:
            new_choice = opponent_choice_dict[opponent_choice] + 1
            if new_choice == 4:
                new_choice = 1
            total_score += new_choice
        
    return total_score
    

def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)
        
    strategy_dict = split_input(lines)
        

    # part one
    total_score = calculate_score(strategy_dict)
    print(total_score)
    
    # part two
    total_score_part_two = calculate_score_part_two(strategy_dict)
    print(total_score_part_two)

if __name__ == '__main__':
    main()