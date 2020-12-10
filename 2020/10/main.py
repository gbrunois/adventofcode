with open("input.txt", "r") as f:
    numbers = [0] + sorted([int(x) for x in f.readlines()])

def diff(input) :
    return [t - s for s, t in zip(input, input[1:])]

def count_paths(diffs):
    count_suite_1 = 0
    result = 1
    # count possible permutation 
    # [3] : 0
    # [1, 3] : 1 
    # [1, 1, 3] : 2
    # [1, 1, 1, 3] : 4
    # [1, 1, 1, 1, 3] : 7
    prod_map = { 0: 1, 1: 1, 2 : 2, 3: 4, 4 : 7 }

    for i in range(0, len(diffs)):
        if diffs[i] == 1:
            count_suite_1 += 1
        else:
            result = result * prod_map[count_suite_1]
            count_suite_1 = 0
    return result


diffs = diff(numbers)
print(diffs)
diff_1 = diffs.count(1)
diff_3 = diffs.count(3)
print(diff_1 , diff_3)
print(count_paths(diffs))

