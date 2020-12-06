from typing import List, Set

def read_groups() -> List[List[str]]:
    groups = []
    current_group = []
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            if line == "":
                groups.append(current_group)
                current_group = []
            else:
                current_group.append(list(line))
        if current_group:
            groups.append(current_group)
    return groups

def intersection(lst1: List, lst2: List) -> List: 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def union(lst1: List, lst2: List) -> List: 
    return list(set(lst1 + lst2))

groups = read_groups()

count = 0
for group in groups:
    answers = group[0]
    for line in group[1:]:
        answers = union(answers, line)
    count = count + len(answers)

print(count)

count = 0
for group in groups:
    answers = group[0]
    for line in group[1:]:
        answers = intersection(answers, line)
    count = count + len(answers)

print(count)

