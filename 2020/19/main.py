from typing import List 

def combine(list1: List[str], list2: List[str]):
    return ["".join([i, j])
        for i in list1
        for j in list2]

def chunked(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def read_file():
    with open("input.txt", "r") as f:
        inputs = f.read().splitlines()
    sep = inputs.index("")
    return inputs[0:sep], inputs[sep+1:]
    
def parse_rules(rules: List[str]):
    rules_dict = {}
    cache = {}

    for rule in rules:
        n, v = rule.split(":")
        rules_dict[int(n)] = v.strip()

    def combine_all(indexes: List[int]):
        result = parse_rule(indexes[0])
        for index in indexes[1:]:
            result = combine(result, parse_rule(index))
        return result

    def parse_rule(index) -> List[str]:
        if index in cache:
            return cache[index]

        rule_str = rules_dict[index]
        result = []

        if '"' in rule_str:
            result = rule_str[rule_str.index('"')+1: rule_str.index('"')+2]
        elif "|" in rule_str:
            left, right = [x.strip() for x in rule_str.split("|")]
            result = combine_all([int(x) for x in left.split(" ")]) + combine_all([int(x) for x in right.split(" ")])  
        else:
            result = combine_all([int(x) for x in rule_str.split(" ")])

        cache[index] = result
        return result

    parse_rule(0)

    return cache

def part_1(rule_set, messages):
    return len([message for message in messages if message in rule_set])

def part_2(rule_set, messages):
    def filter(message):
        rule_42 = rule_set[42]
        rule_31 = rule_set[31]

        # 0: 8 11
        # 8: 42 | 42 8        
        # 11: 42 31 | 42 11 31

        # [42] [42] [31]      
        # [42] [42] [42]* [31]* [31]

        # [42] [42] [31] [31] [31] => false
        # [42] [42] [42] [31] [31] => true
        # [42] [42] [42] [42] [31] [31] [31] => true

        chunks = list(chunked(message, 8))

        # first and second chunk must match rule 42, last chunck must match rule 31
        if (not chunks[0] in rule_42) or (not chunks[1] in rule_42) or (not chunks[-1] in rule_31):
            return False
        # must match a least one more rule 42
        first_chunk_not_matching_42 = chunks.index([c for c in chunks if not c in rule_42][0])
        
        if first_chunk_not_matching_42 <= (len(chunks) - first_chunk_not_matching_42):
            return False
        # all other chunks must match rule 31
        return all(map(lambda t: t in rule_31, chunks[first_chunk_not_matching_42:]))

    return len([message for message in messages if filter(message)])

rules, messages = read_file()
rule_set = parse_rules(rules)

print(part_1(rule_set[0], messages))
print(part_2(rule_set, messages))