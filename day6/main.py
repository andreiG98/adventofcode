import os
import re

import queue

def read_file(file_path):
    
    with open(file_path) as file:
        lines = [line.rstrip() for line in file]
        
    return lines


def first_marker(packet, marker_len=4):

    for idx in range(len(packet) - marker_len + 1):
        packet_set = set(packet[idx:idx + marker_len])

        if len(packet_set) == marker_len:
            marker_start = idx + marker_len
            
            return marker_start

    return None


def main():
    file_path = os.path.join(os.getcwd(), 'input.txt')
    lines = read_file(file_path=file_path)

    start_of_the_packet = first_marker(lines[0])
    print(start_of_the_packet)

    start_of_the_message = first_marker(lines[0], marker_len=14)
    print(start_of_the_message)

if __name__ == '__main__':
    main()