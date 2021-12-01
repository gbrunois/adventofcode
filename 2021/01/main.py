def part01(inputs):
    previous = inputs[0]
    count = 0
    for x in inputs[1:]:
        if int(x) > previous:
            count += 1
        previous = x

    print(count)


def part02(inputs):
    previous_window = [inputs[0], inputs[1], inputs[2]]
    count = 0
    for index, value in enumerate(inputs[1:-1]):
        current_window = [inputs[index], inputs[index+1], inputs[index+2]]
        if sum(current_window) > sum(previous_window):
            count += 1
        previous_window = current_window
    print(count)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [int(x) for x in f.readlines()]
    part01(inputs)
    #part02(inputs)


