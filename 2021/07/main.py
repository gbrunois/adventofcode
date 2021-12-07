def calculate(inputs):
    lowest = min(inputs)
    highest = max(inputs)

    fuels = {}
    fuels_part2 = {}
    for i in range(lowest, highest+1):
        fuels[i] = 0
        fuels_part2[i] = 0
        for num in inputs:
            if num > i:
                n = num - i
            else:
                n = i - num
            fuels[i] += n
            fuels_part2[i] += (n * (n+1))/2
    print(min(fuels.values()))
    print(min(fuels_part2.values()))


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x for x in f.readlines()]
    numbers = [int(i) for i in inputs[0].strip("\n").split(",")]
    calculate(numbers)


