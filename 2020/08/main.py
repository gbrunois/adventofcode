import re

p = re.compile('^([a-z]{3}) (-|\+){1}(\d+)$')

with open("input.txt", "r") as f:
    instructions = [p.match(x).groups() for x in f.readlines()]

jumps = [index for index, instruction in enumerate(instructions) if instruction[0] == "jmp"]


def execute(ignore_jump_index: int):
    value = 0
    index = 0
    is_infinite_loop = False
    stack = []
    while not index in stack and index < len(instructions):
        op, sign, str_v = instructions[index]
        v = int(str_v)
            
        stack.append(index)
        
        if op == "acc":
            if sign == "+":
                value = value + v
            else:
                value = value - v
        if op == "jmp" and not index == ignore_jump_index:
            if sign == "+":
                index = index + v
            else:
                index = index - v
        else:
            index = index +1

        if index in stack:
            is_infinite_loop = True
    return value, is_infinite_loop

inf = True
jump_index = 0
while inf == True:
    v, inf = execute(jumps[jump_index])
    jump_index = jump_index + 1
    print(v, inf)