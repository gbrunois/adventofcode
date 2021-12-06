def calculate(inputs, days):
    fish_clocks = init_fish_clocks()
    for i in inputs:
        fish_clocks[i] += 1

    for i in range(days):
        fish_clocks = next_day(fish_clocks)
    print(sum(fish_clocks.values()))


def init_fish_clocks():
    fish = {}
    for i in range(9):
        fish[i] = 0
    return fish


def next_day(fish_clocks):
    new_fish_clocks = init_fish_clocks()
    for k, v in fish_clocks.items():
        if k == 0:
            new_fish_clocks[6] += v
            new_fish_clocks[8] += v
        else:
            new_fish_clocks[k-1] += v
    return new_fish_clocks


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x for x in f.readlines()]
    numbers = [int(i) for i in inputs[0].strip("\n").split(",")]
    calculate(numbers, 80)
    calculate(numbers, 256)


