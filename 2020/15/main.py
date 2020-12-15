# turn 1 : 0
# turn 2 : 3
# turn 3 : 6
# turn 4 : 0 (last is new)
# turn 5 : [4] - [1] : 3 (age)
# turn 6 : [5] - [2] : 3
# turn 7 : [6] - [5] : 1
# turn 8: 0 (last is new)
# turn 9 : [8] - [4] = 4
# turn 10 : 0 (last is new)
# turn 2020: 436

#init = [0, 3, 6]
init = [6,19,0,5,7,13,1]

last_occurs = { v: [i+1] for i, v in enumerate(init)}

previous = None
current = list(last_occurs.keys())[-1]

for i in range(len(init)+1, 30000000 + 1):
    previous = current
    last_occur = last_occurs.get(previous)
    if not last_occur or len(last_occur) == 1:
        current = 0
    else:
        current = last_occurs[previous][-1] - last_occurs[previous][-2]
    
    if last_occurs.get(current):
        last_occurs[current].append(i)
    else:
        last_occurs[current] = [i]

print(current)

