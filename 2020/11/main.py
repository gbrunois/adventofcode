from typing import List

with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

def print_grid(grid):
    for line in grid:
        print(line)

def get_adjacents(grid, line_idx: int, seat_idx: int) -> List[str]:
    adjacents = []
    grid_width = len(grid[0])
    if line_idx > 0:
        if seat_idx > 0:
            adjacents.append(grid[line_idx-1][seat_idx-1])
        adjacents.append(grid[line_idx-1][seat_idx])
        if seat_idx < grid_width - 1:
            adjacents.append(grid[line_idx-1][seat_idx+1])
    if seat_idx > 0:
        adjacents.append(grid[line_idx][seat_idx-1])
    if seat_idx < grid_width - 1:
        adjacents.append(grid[line_idx][seat_idx+1])
    if line_idx < len(grid) - 1:
        if seat_idx > 0:
            adjacents.append(grid[line_idx+1][seat_idx-1])
        adjacents.append(grid[line_idx+1][seat_idx])
        if seat_idx < grid_width - 1:
            adjacents.append(grid[line_idx+1][seat_idx+1])
    return adjacents

def first_seat_left(grid, line_idx: int, seat_idx: int):
    i = seat_idx - 1
    while i >= 0:
        if grid[line_idx][i] != ".":
            return grid[line_idx][i]
        i -= 1
    return None

def first_seat_right(grid, line_idx: int, seat_idx: int):
    i = seat_idx + 1
    grid_width = len(grid[0])
    while i < grid_width:
        if grid[line_idx][i] != ".":
            return grid[line_idx][i]
        i += 1
    return None

def first_seat_up(grid, line_idx: int, seat_idx: int):
    i = line_idx - 1
    while i >= 0:
        if grid[i][seat_idx] != ".":
            return grid[i][seat_idx]
        i -= 1
    return None

def first_seat_bottom(grid, line_idx: int, seat_idx: int):
    i = line_idx + 1
    while i < len(grid):
        if grid[i][seat_idx] != ".":
            return grid[i][seat_idx]
        i += 1
    return None

def first_seat_diag1(grid, line_idx: int, seat_idx: int):
    i = seat_idx - 1
    j = line_idx - 1
    while j >= 0 and i >= 0:
        if grid[j][i] != ".":
            return grid[j][i]
        i -= 1
        j -= 1
    return None

def first_seat_diag2(grid, line_idx: int, seat_idx: int):
    i = seat_idx + 1
    j = line_idx - 1
    grid_width = len(grid[0])
    while j >= 0 and i < grid_width:
        if grid[j][i] != ".":
            return grid[j][i]
        i += 1
        j -= 1
    return None

def first_seat_diag3(grid, line_idx: int, seat_idx: int):
    i = seat_idx - 1
    j = line_idx + 1
    while j < len(grid) and i >= 0:
        if grid[j][i] != ".":
            return grid[j][i]
        i -= 1
        j += 1
    return None

def first_seat_diag4(grid, line_idx: int, seat_idx: int):
    i = seat_idx + 1
    j = line_idx + 1
    grid_width = len(grid[0])
    while j < len(grid) and i < grid_width:
        if grid[j][i] != ".":
            return grid[j][i]
        i += 1
        j += 1
    return None

def first_visibles_seats(grid, line_idx: int, seat_idx: int) -> List[str]:
    visibles = []
    visibles.append(first_seat_left(grid, line_idx, seat_idx))
    visibles.append(first_seat_right(grid, line_idx, seat_idx))
    visibles.append(first_seat_up(grid, line_idx, seat_idx))
    visibles.append(first_seat_bottom(grid, line_idx, seat_idx))
    visibles.append(first_seat_diag1(grid, line_idx, seat_idx))
    visibles.append(first_seat_diag2(grid, line_idx, seat_idx))
    visibles.append(first_seat_diag3(grid, line_idx, seat_idx))
    visibles.append(first_seat_diag4(grid, line_idx, seat_idx))
    return visibles

def apply_moves_ex1(grid: List[str]) -> List[str]:
    new_grid = []
    grid_width = len(grid[0])
    for line_idx in range(len(grid)):
        new_line = []
        for seat_idx in range(grid_width):
            c = grid[line_idx][seat_idx]
            if c != ".":
                adjacents = get_adjacents(grid, line_idx, seat_idx)
                if c == "L":
                    # no occupied
                    if adjacents.count("#") == 0:
                        c = "#"
                elif c == "#":
                    # four or more also occupied
                    if adjacents.count("#") >= 4:
                        c = "L"
            new_line.append(c)
        new_grid.append(''.join(new_line))
    return new_grid

def apply_moves_ex2(grid: List[str]) -> List[str]:
    new_grid = []
    grid_width = len(grid[0])
    for line_idx in range(len(grid)):
        new_line = []
        for seat_idx in range(grid_width):
            c = grid[line_idx][seat_idx]
            if c != ".":
                first_visibles = first_visibles_seats(grid, line_idx, seat_idx)
                if c == "L":
                    # no occupied
                    if first_visibles.count("#") == 0:
                        c = "#"
                elif c == "#":
                    # five or more also occupied
                    if first_visibles.count("#") >= 5:
                        c = "L"
            new_line.append(c)
        new_grid.append(''.join(new_line))
    return new_grid

def are_equals(grid_a: List[str], grid_b: List[str]) -> bool:
    for line_idx in range(len(grid_a)):
        if grid_a[line_idx] != grid_b[line_idx]:
            return False
    return True

def count_occupied_seats(grid: List[str]) -> int:
    return sum([line.count("#") for line in grid])

def ex1():
    stable = False
    grid = inputs
    while not stable:
        new_grid = apply_moves_ex1(grid)
        stable = are_equals(grid, new_grid)
        grid = new_grid
    return count_occupied_seats(grid)

def ex2():
    stable = False
    grid = inputs
    while not stable:
        new_grid = apply_moves_ex2(grid)
        stable = are_equals(grid, new_grid)
        grid = new_grid
    return count_occupied_seats(grid)

print(ex1())
print(ex2())