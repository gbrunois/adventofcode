def eval_part_1(expression):
    firstClosingParen = 0

    if ")" in expression:
        firstClosingParen = expression.index(")")
        lastOpeningParen = firstClosingParen - 1
        while (expression[lastOpeningParen] != "("):
            lastOpeningParen -= 1
            if lastOpeningParen < 0:
                raise Exception("Parse error")

        result = eval_part_1(expression[lastOpeningParen + 1: firstClosingParen])
        return eval_part_1(expression[0: lastOpeningParen] + str(result) + expression[firstClosingParen + 1:])
    else:
        fields = expression.split(" ")
        index = 0
        result = None
        while (index < len(fields) - 1):
            op1 = int(fields[index])
            op2 = int(fields[index + 2])
            result = op1 + op2 if fields[index + 1] == "+" else op1 * op2
            fields[index + 2] = str(result)
            index += 2
        return result

def eval_part_2(expression):
    firstClosingParen = 0
        
    if ")" in expression:
        firstClosingParen = expression.index(")")
        lastOpeningParen = firstClosingParen - 1
        while (expression[lastOpeningParen] != "("):
            lastOpeningParen -= 1
            if lastOpeningParen < 0:
                raise Exception("Parse error")

        result = eval_part_2(expression[lastOpeningParen + 1: firstClosingParen])
        return eval_part_2(expression[0: lastOpeningParen] + str(result) + expression[firstClosingParen + 1:])
        
    else:
        
        fields = expression.split(" ")
        result = None
        while(len(fields) > 2):
            opIndex = fields.index("+") if "+" in fields else fields.index("*")
            op1 = int(fields[opIndex-1])
            op2 = int(fields[opIndex + 1])
            result = op1 + op2 if fields[opIndex] == "+" else op1 * op2
            fields = fields[:opIndex-1] + [str(result)] + fields[opIndex+2:]
        
        return result

def parse_lines():
    with open("input.txt") as f:
        return f.read()

def part_1(input: str):
    return sum([eval_part_1(line) for line in input.splitlines()])

def part_2(input: str):
    return sum([eval_part_2(line) for line in input.splitlines()])

print(part_1(parse_lines())) 
print(part_2(parse_lines())) 