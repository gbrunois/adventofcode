from typing import Tuple

def find_coordinate(range: Tuple[int, int], code):
    current_range = range
    for char in code:
        start, end = current_range
        middle = int((end - start + 1) / 2) + start
        range_part1 = (start, middle -1)
        range_part2 = (middle, end)

        if char == "F" or char == "L":
            current_range = range_part1
        else:
            current_range = range_part2

    return current_range[0]


with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

seat_ids = []
for seat_code in inputs:
    row = find_coordinate((0,127), seat_code[0:7])
    column = find_coordinate((0,7), seat_code[7:10])
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids.sort()
print(f"Highest is {seat_ids[len(seat_ids) - 1]}")

id_found = None
for index, id in enumerate(seat_ids):
    if index < len(seat_ids) - 1 and seat_ids[index]+1 != seat_ids[index+1]:
        id_found = seat_ids[index]+1
print(f"My seat is {id_found}")