import re

p = re.compile('^(\d+)-(\d+) ([a-z]): ([a-z]+)$')

with open("input.txt", "r") as f:
     inputs = [p.match(x).groups() for x in f.readlines()]

count = 0
for min, max, char, input in inputs:
    if input.count(char) >= int(min) and input.count(char) <= int(max):
        count = count + 1
print(count)

count = 0
for min, max, char, input in inputs:
    char1 = input[int(min)-1]
    char2 = input[int(max)-1]
    if not char1 == char2 and (char1 == char or char2 == char):
        count = count + 1
print(count)