def part01(inputs):
    horizontal = 0
    depth = 0
    for x in inputs:
        action, value = x.split(' ', 1)
        if action == "forward":
            horizontal += int(value)
        if action == "down":
            depth += int(value)
        if action == "up":
            depth -= int(value)

    print(horizontal * depth)


def part02(inputs):
    horizontal = 0
    depth = 0
    aim = 0
    for x in inputs:
        action, value = x.split(' ', 1)
        if action == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        if action == "down":
            aim += int(value)
        if action == "up":
            aim -= int(value)

    print(horizontal * depth)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x for x in f.readlines()]
    part01(inputs)
    part02(inputs)


