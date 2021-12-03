def part01(inputs):
    gamma_rate = []
    epsilon_rate = []
    size = len(inputs[0]) - 1
    for pos in range(size):
        count_bit0 = 0
        count_bit1 = 0
        for number in inputs:
            if number[pos] == "1":
                count_bit1 += 1
            else:
                count_bit0 += 1
        if count_bit1 > count_bit0:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)
    gamma = int("".join(str(x) for x in gamma_rate), 2)
    epsilon = int("".join(str(x) for x in epsilon_rate), 2)
    print(gamma * epsilon)


def part02(inputs):
    i = inputs
    pos = 0
    while len(i) > 1:
        i = filter(i, pos, take_bit1=True)
        pos += 1

    j = inputs
    pos = 0
    while len(j) > 1:
        j = filter(j, pos, take_bit1=False)
        pos += 1
    oxygen = int(i[0], 2)
    co2 = int(j[0], 2)
    print(oxygen * co2)


def filter(inputs, pos: int, take_bit1: bool):
    count_bit0 = 0
    count_bit1 = 0
    with_0 = []
    with_1 = []
    for number in inputs:
        if number[pos] == "1":
            count_bit1 += 1
            with_1.append(number)
        else:
            count_bit0 += 1
            with_0.append(number)
    if take_bit1:
        if count_bit1 >= count_bit0:
            return with_1
        else:
            return with_0
    else:
        if count_bit1 < count_bit0:
            return with_1
        else:
            return with_0


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x for x in f.readlines()]
    part01(inputs)
    part02(inputs)


