import re


def part01(inputs):
    numbers = inputs[0].rstrip("\n").split(",")
    grids = build_grids(inputs)

    has_winner = False
    winner_number = None
    winner_grid = None
    for number in numbers:
        for grid in grids:
            for line in grid:
                for i, v in enumerate(line):
                    if v == number:
                        line[i] = "X"
            if is_winner(grid):
                winner_grid = grid
                has_winner = True
                break
        if has_winner:
            winner_number = number
            break

    sum_values = sum_remaining_values(winner_grid)

    print(sum_values * int(winner_number))


def part02(inputs):
    numbers = inputs[0].rstrip("\n").split(",")
    grids = build_grids(inputs)

    winner_number = None
    winner_grid = None
    remaining_grids = grids
    for number_index, number in enumerate(numbers):
        if len(remaining_grids) == 0:
            break
        for grid_index, grid in enumerate(remaining_grids):
            for line in grid:
                for i, v in enumerate(line):
                    if v == number:
                        line[i] = "X"
        for grid_index, grid in enumerate(remaining_grids):
            if is_winner(grid):
                remaining_grids.remove(grid)
        if len(remaining_grids) == 1:
            winner_grid = remaining_grids[0]
            winner_number = numbers[number_index+1]

    sum_values = sum_remaining_values(winner_grid)
    print(sum_values * int(winner_number))


def build_grids(inputs):
    grids = []
    i = 0
    grid = []
    for line in inputs[2:]:
        if line == "\n":
            i = i + 1
            grids.append(grid)
            grid = []
        else:
            grid.append(re.findall(r'\S+', line.rstrip("\n")))
    grids.append(grid)
    return grids


def is_winner(grid):

    for line in grid:
        if all([i == "X" for i in line]):
            return True

    for col in range(len(grid[0])):
        values = [line[col] for line in grid]
        if all([i == "X" for i in values]):
            return True
    return False


def sum_remaining_values(winner_grid):
    sum_values = 0
    for line in winner_grid:
        for i, v in enumerate(line):
            if v != "X":
                sum_values += int(v)
    return sum_values


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x for x in f.readlines()]

    part01(inputs)
    part02(inputs)


