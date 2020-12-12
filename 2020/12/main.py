from enum import Enum

with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

def turn(direction: Direction, angle: int):
    n = (int(angle / 90) + direction.value) % 4
    return Direction(n)

direction_values = ["E", "S", "W", "N"]

def ex1():
    current_direction = Direction.EAST
    current_position = (0, 0)
    for input in inputs:
        action = input[0]
        value = int(input[1:])
        current_east = current_position[0]
        current_north = current_position[1]

        if action == "F":
            action = direction_values[current_direction.value]

        if action == "N":
            current_north += value
        if action == "S":
            current_north -= value
        if action == "E":
            current_east += value
        if action == "W":
            current_east -= value

        current_position = (current_east, current_north)

        if action == "R":
            current_direction = turn(current_direction, value)
        if action == "L":
            current_direction = turn(current_direction, -value)

    return abs(current_position[0]) + abs(current_position[1])

def turn_way_point(coor, angle):
    n = (int(angle / 90)) % 4
    if n == 0:
        return coor
    if n == 1:
        return (coor[1], -coor[0])
    if n == 2:
        return (-coor[0], -coor[1])
    if n == 3:
        return (-coor[1], coor[0])

def ex2():
    current_position = (0, 0)
    way_point = (10, 1)
    for input in inputs:
        action = input[0]
        value = int(input[1:])

        if action == "F":
            current_east = current_position[0]
            current_north = current_position[1]
            current_east += way_point[0] * value
            current_north += way_point[1] * value
            current_position = (current_east, current_north)
        else:
            if action == "R":
                way_point = turn_way_point(way_point, value)
            elif action == "L":
                way_point = turn_way_point(way_point, -value)
            else:
                current_east = way_point[0]
                current_north = way_point[1]

                if action == "N":
                    current_north += value
                if action == "S":
                    current_north -= value
                if action == "E":
                    current_east += value
                if action == "W":
                    current_east -= value
                way_point = (current_east, current_north)

    return abs(current_position[0]) + abs(current_position[1])

print(ex1())
print(ex2())
