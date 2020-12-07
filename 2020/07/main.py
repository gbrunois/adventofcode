import re
from typing import List

rule_re = re.compile('^([a-z]+ [a-z]*) bags? contain (.*)$')
rule_part_re = re.compile(' ?(\d+) ([a-z]+ [a-z]*) bags?\.?')

rules = {}
with open("input.txt", "r") as f:
     for rule in f.readlines():
        if not rule_re.match(rule):
            raise Exception(str(rule))
        groups = rule_re.match(rule).groups()
        rules[groups[0]] = {}
        if groups[1] != "no other bags.":
            rule_parts = groups[1].split(",")
            for rule_part in rule_parts:
                if not rule_part_re.match(rule_part):
                    raise Exception(str(rule_part))
                sub_rule_groups = rule_part_re.match(rule_part).groups()
                rules[groups[0]][sub_rule_groups[1]] = int(sub_rule_groups[0])


def list_colors(color) -> List[str]:
    bag_colors = []
    
    for rule_color in rules.keys():
        if color in rules[rule_color].keys():
            bag_colors.append(rule_color)
            bag_colors = bag_colors + list_colors(rule_color)
    return list(set(bag_colors))

total_count = len(list_colors("shiny gold"))
print(f"{total_count} bag colors can eventually contain at least one shiny gold bag")

def required_inside(color: str):
    if not rules.get(color) or rules[color] == 0:
        return 0
    result = 0
    for sub_color in rules[color].keys():
        number = rules[color][sub_color]
        result = result + number + number * required_inside(sub_color)
    return result

print(f"{required_inside('shiny gold')} individual bags are required inside your single shiny gold bag")


