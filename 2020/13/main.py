import math

with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

def ex1():
    timestamp = int(inputs[0])
    bus_ids = [int(id) for id in inputs[1].split(',') if id != 'x']

    next_times = [(math.ceil(timestamp / bus_id) * bus_id, bus_id) for bus_id in bus_ids]
    next_time = min(next_times)
    print((next_time[0] - timestamp) * next_time[1])


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def ex2():

    bus_ids = [(index, int(id)) for index, id in enumerate(inputs[1].split(',')) if id != 'x']
    print(bus_ids)

    timestamp = 0
    step = 1

    for bus_id in bus_ids:
        while (timestamp + bus_id[0]) % bus_id[1] != 0:
            timestamp += step

        step = lcm(step, bus_id[1])

    return timestamp

print(ex2())