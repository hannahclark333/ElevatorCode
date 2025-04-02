'''
Assumptions made: 
1.) The elevator will go downward first, then upward.
2.) The input is given in the form of space separated integers. 
'''

import sys
import re

# inputs are start floor and list of floors to visit

# output is total travel time and list of floors visited in order

# constant floor travel time
floor_travel_time = 10

def main():
    # get inputs
    inputs = sys.argv[1:]

    start_floor = int(inputs[0])
    floors_to_visit = list(map(int, inputs[1:]))

    # Problem from Example

    print(elevator(start_floor, floors_to_visit))

    return 0

# function to perform time of elevator
def elevator(start, floors) :
    total_time = 0
    floors_visited = []

    floors_below = sorted([x for x in floors if x < start], reverse=True) 
    floors_above = sorted([x for x in floors if x > start])

    floors_visited.append(start)
    current_floor = start
    # travel downward
    for floor in floors_below :
        difference = current_floor - floor
        total_time += (floor_travel_time * difference)
        current_floor = floor
        floors_visited.append(floor)

    # travel upward
    for floor in floors_above :
        difference = floor - current_floor
        total_time += (floor_travel_time * difference)
        current_floor = floor
        floors_visited.append(floor)
    
    return total_time, floors_visited

# function to perform time of elevator
def elevator_with_button(start, floors, button) :

    return start


if __name__ == '__main__':
  main()
