from typing import Tuple
import numpy as np


def get_neighbors(inputs, y, x) -> [Tuple[int, int]]:
    n = []
    if y > 0:
        n.append((y-1, x))
    if y < len(inputs) - 1:
        n.append((y+1, x))
    if x > 0:
        n.append((y, x-1))
    if x < len(inputs[0]) - 1:
        n.append((y, x+1))
    return n


def grow(inputs, coord, bassin):
    if coord in bassin:
        return
    if inputs[coord[0]][coord[1]] == "9":
        return
    else:
        bassin.append(coord)
        neighbors = get_neighbors(inputs, coord[0], coord[1])
        for n in neighbors:
            grow(inputs, n, bassin)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x.strip() for x in f.readlines()]

    lowest = []
    lowest_coord = []
    for i, line in enumerate(inputs):
        for j, value in enumerate(line):
            neighbors_values = map(lambda c: int(inputs[c[0]][c[1]]), get_neighbors(inputs, i, j))

            if int(value) < min(neighbors_values):
                lowest.append(int(value))
                lowest_coord.append((i, j))

    bassin_sizes = []
    for coord in lowest_coord:
        bassin = []
        grow(inputs, coord, bassin)
        bassin_sizes.append(len(bassin))

    print(sum(map(lambda x: x + 1, lowest)))
    print(np.prod(list(sorted(bassin_sizes, reverse=True)[0:3])))


