with open("input.txt", "r") as f:
    inputs = [int(x) for x in f.readlines()]

for x in inputs:
    if x < 2020:
        r = 2020 - x
        if r in inputs:
            print(r*x)

for i, x in enumerate(inputs):
    for j, y in enumerate(inputs, start=i):
        if x + y < 2020:
            r = 2020 - x - y
            if r in inputs:
                print(r*x*y)