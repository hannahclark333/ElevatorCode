'''
Assumptions made: 
1.) The elevator will go downward first, then upward.
2.) The input is given in the form of space separated integers. 
3.) That the input is overall valid, no character values are given.
4.) Floor values are numbers 1 and above. Implemetation of basement levels would require the
addition of either handling negatives or floors presented in the B# format.
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

    # Checks for type of call button pressed
    # Although this is checked, the button type is not further implemeneted

    if len(floors_below) == 0 and len(floors_above) == 0:
        return total_time, start
    
    elif len(floors_below) == 0:
        button_type = "up"

        # travel upward
        for floor in floors_above :
            difference = floor - current_floor
            total_time += (floor_travel_time * difference)
            current_floor = floor
            floors_visited.append(floor)
            
    elif len(floors_above) == 0:
        button_type = "down"

        # travel downward
        for floor in floors_below :
            difference = current_floor - floor
            total_time += (floor_travel_time * difference)
            current_floor = floor
            floors_visited.append(floor)
                
    else:
        button_type = "both"

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

    # With further time for implementation after the button call is evaluated this function
    # Could be further developed to reduce the number of iterations and repetition of code
    return button


if __name__ == '__main__':
  main()
