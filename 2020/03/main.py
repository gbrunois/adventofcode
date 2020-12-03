slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]

with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

def print_map_coord(pos):
    x, y = pos
    line_length = len(inputs[0])
    value = (inputs[y][x%line_length])
    if value == '.':
        return "O"
    else:
        return "X"

cumul = 1

for right, down in slopes:

    count_trees = 0
    cur_x = 0
    cur_y = 0
    cur_x = cur_x + right
    cur_y = cur_y + down
    while cur_y < len(inputs):
        v = print_map_coord((cur_x, cur_y))
        if v == "X":
            count_trees = count_trees + 1
        cur_x = cur_x + right
        cur_y = cur_y + down

    print(count_trees)
    cumul = count_trees * cumul

print(cumul)

