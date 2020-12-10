with open("input.txt", "r") as f:
    numbers = [int(x) for x in f.readlines()]

preamble_len = 5

def find_invalid():
    preamble = numbers[0:preamble_len]
    index = 0
    for num in numbers[preamble_len:]:
        is_valid = False
        for num_p in preamble:
            if (num - num_p != num_p) and (num - num_p) in preamble:
                is_valid = True
        if not is_valid:
            return num
        index = index + 1
        preamble = numbers[index:preamble_len+index]

def find_pair(invalid_number):
    # find the continuos list that sums the invalid_number
    for i in range(len(numbers) - 1):
        smallest = numbers[i]
        largest = numbers[i]
        sum = numbers[i]
        for j in range(i+1, len(numbers)):
            sum += numbers[j]
            if sum > invalid_number:
                break
            if numbers[j] > largest:
                largest = numbers[j]
            if numbers[j] < smallest:
                smallest = numbers[j]
            if sum == invalid_number:
                return smallest, largest, smallest + largest
    
invalid = find_invalid()
print(invalid)
print(find_pair(invalid))