
def calculate(inputs, handle_diagonals: bool):
    lines = [line.strip("\n").split(" -> ") for line in inputs]
    diagram = {}
    for line in lines:
        start_coordinates = line[0].split(",")
        end_coordinates = line[1].split(",")

        x1 = int(start_coordinates[0])
        x2 = int(end_coordinates[0])

        y1 = int(start_coordinates[1])
        y2 = int(end_coordinates[1])

        if x1 == x2:
            if y1 < y2:
                incr = 1
            else:
                incr = -1

            for y in range(y1, y2 + incr, incr):
                diagram[(x1, y)] = diagram.get((x1, y), 0) + 1
        elif y1 == y2:
            if x1 < x2:
                incr = 1
            else:
                incr = -1

            for x in range(x1, x2 + incr, incr):
                diagram[(x, y1)] = diagram.get((x, y1), 0) + 1
        elif handle_diagonals:
            if x1 < x2:
                if y1 < y2:
                    incr = 1
                else:
                    incr = -1

                y = y1
                for x in range(x1, x2 + 1):
                    diagram[(x, y)] = diagram.get((x, y), 0) + 1
                    y = y + incr
            else:
                if y1 < y2:
                    incr = 1
                else:
                    incr = -1

                y = y1
                for x in range(x1, x2 - 1, -1):
                    diagram[(x, y)] = diagram.get((x, y), 0) + 1
                    y = y + incr

    print(len([x for x in diagram.values() if x > 1]))


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        inputs = [x for x in f.readlines()]
    calculate(inputs, handle_diagonals=False)
    calculate(inputs, handle_diagonals=True)


