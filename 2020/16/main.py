import re
from typing import Dict, List, Tuple
from functools import reduce

rules = []


class Rule:

    def __init__(self, name: str, range_1: Tuple[int, int], range_2: Tuple[int, int]):
        self.name = name
        self.range_1 = range_1
        self.range_2 = range_2

    def is_in_range(self, value: int):
        return value >= self.range_1[0] and value <= self.range_1[1] \
               or value >= self.range_2[0] and value <= self.range_2[1]

    def __repr__(self) -> str:
        return self.name

class Run():

    def __init__(self) -> None:
        self.read_file()

    def read_file(self):
        self.rules = []
        self.nearby_tickets = []
        self.my_ticket = []
        rule_re = re.compile("^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$")
        with open("input.txt", "r") as f:
            part = 0
            for line in f.read().splitlines():
                if line == "your ticket:":
                    part = 1
                    continue
                if line == "nearby tickets:":
                    part = 2
                    continue
                if line == "":
                    continue

                if part == 0 and rule_re.match(line):
                    rule_grp = rule_re.match(line).groups()
                    rules.append(Rule(
                        rule_grp[0], 
                        (int(rule_grp[1]), int(rule_grp[2])),
                        (int(rule_grp[3]), int(rule_grp[4])))
                    )
                if part == 1:
                    self.my_ticket = [int(x) for x in line.split(",")]
                if part == 2:
                    self.nearby_tickets.append([int(x) for x in line.split(",")])

    def find_invalid_numbers(self):
        self.invalid_numbers = []
        self.valid_tickets = [self.my_ticket]
        for nearby_ticket in self.nearby_tickets:
            contains_invalid_number = False
            for number in nearby_ticket:
                is_valid = False
                for r in rules:
                    if r.is_in_range(number):
                        is_valid = True
                if not is_valid:
                    contains_invalid_number = True
                    self.invalid_numbers.append(number)
            if not contains_invalid_number:
                self.valid_tickets.append(nearby_ticket)

    def find_ticket_field_values(self)-> Dict[str, int]:
        maches_fields = {} # key is index, value is list of possible field name
        fields_found = {} # key is field name, value is ticket field value
        for i in range(0, len(self.my_ticket)):
            field_values = [v[i] for v in self.valid_tickets]
            matching_rules = [rule 
                              for rule in rules
                              if all([rule.is_in_range(v) for v in field_values])
                             ]
            maches_fields[i] = [r.name for r in matching_rules]

        while len(fields_found) < len(rules):
            for i in maches_fields.keys():
                if len(maches_fields[i]) == 1:
                    fields_found[maches_fields[i][0]] = self.my_ticket[i]
            for i in maches_fields.keys():
                # remove found field name
                maches_fields[i] = [v for v in maches_fields[i] if not v in list(fields_found.keys())]

        return fields_found

run = Run()
run.find_invalid_numbers()
print(f"Sum of invalid numbers: {sum(run.invalid_numbers)}")

values = [v for name, v in run.find_ticket_field_values().items() if "departure" in name]
print(f"Multiply of departure values: {reduce(lambda x, y: x * y, values)}")