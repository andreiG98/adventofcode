import os


def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.strip() for line in file]
        
    return lines


def parse_input(input):
    valves = dict()

    for line in input:
        try:
            rest_line, connected_valves_string = line.split("valves")
        except ValueError:
            rest_line, connected_valves_string = line.split("valve")

        connected_valves_list = connected_valves_string.split(",")
        connected_valves_list = list(map(str.strip, connected_valves_list))        

        _, valve_name, _, _, rate, _, _, _, _ = rest_line.split(" ")

        rate = int(rate.split("=")[1].replace(";", ""))

        valves[valve_name] = {
            "pressure": rate,
            "connections": connected_valves_list
        }


def main():
    file_path = os.path.join(os.getcwd(), 'input2.txt')
    lines = read_file(file_path=file_path)

    valves = parse_input(lines)

    

if __name__ == '__main__':
    main()