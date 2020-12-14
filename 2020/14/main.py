import re
from typing import List


with open("input.txt", "r") as f:
    inputs = f.read().splitlines()

mask_re = re.compile('^mask = ([X0-1]*)$')
ins_re = re.compile('^mem\[(\d+)\] = (\d+)$')

def ex1():
    mask = None
    memory = {}

    def apply_mask(mask: str, value: str) -> int:
        return int("".join([m if m != "X" else n for m, n in zip(mask, value)]), 2)

    for input in inputs:
        if input.startswith("mask"):
            mask = mask_re.match(input).groups()[0]
        else:
            adress = int(ins_re.match(input).groups()[0])
            value = format(int(ins_re.match(input).groups()[1]), "b").zfill(len(mask))
            memory[adress] = apply_mask(mask, value)
    
    return sum(memory.values())

def ex2():
    mask = None
    memory = {}

    def apply_mask(mask: str, adress: str) -> List[int]:
        new_adresses = []
        new_adress_mask = "".join([n if m == "0" else m for m, n in zip(mask, adress)])
        count_x = new_adress_mask.count("X")
        replacements = [format(i, "b").zfill(count_x) for i in range(2**count_x)]
        
        for replacement in replacements:
            new_adress = new_adress_mask[:]
            for bit in replacement:
                bit_index = new_adress.find("X")
                new_adress = list(new_adress)
                new_adress[bit_index] = bit
                new_adress = "".join(new_adress)
            new_adresses.append(int(new_adress,2))
        return new_adresses

    for input in inputs:
        if input.startswith("mask"):
            mask = mask_re.match(input).groups()[0]
        else:
            adress = format(int(ins_re.match(input).groups()[0]), "b").zfill(len(mask))
            value = int(ins_re.match(input).groups()[1])
            adresses = apply_mask(mask, adress)
            for adr in adresses:
                memory[adr] = value
    
    return sum(memory.values())

print(ex1())
print(ex2())
