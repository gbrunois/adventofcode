
from typing import List
import re

p = re.compile('([a-z]{3}):(\S+)')

def parse_line(line) -> dict:
    d = {}
    for key, value in p.findall(line):
        d[key] = value
    return d

def read_passports() -> List[dict]:
    passports = []
    passport = {}
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            if line == "":
                if passport:
                    passports.append(passport)
                passport = {}
            else:
                passport.update(parse_line(line))
        if passport:
            passports.append(passport)
    return passports


four_digit_re = re.compile('^\d{4}$')
height_re = re.compile('^(\d+)(cm|in)$')
color_re = re.compile('^#[a-f0-9]{6}$')
pid_re = re.compile('^\d{9}$')

def validate_byr(byr: str):
    if not four_digit_re.match(byr):
        return False
    value = int(byr)
    return value >= 1920 and value <= 2002

def validate_iyr(iyr: str):
    if not four_digit_re.match(iyr):
        return False
    value = int(iyr)
    return value >= 2010 and value <= 2020

def validate_eyr(eyr: str):
    if not four_digit_re.match(eyr):
        return False
    value = int(eyr)
    return value >= 2020 and value <= 2030

def validate_hgt(hgt: str):
    match = height_re.match(hgt)
    if not match:
        return False
    h = int(match.groups()[0])
    unit = match.groups()[1]
    if unit == "cm":
        return h >= 150 and h <= 193
    else:
        return h >= 59 and h <= 76


def validate_hcl(hcl: str):
    return color_re.match(hcl)

def validate_ecl(ecl: str):
    return ecl in ["amb","blu", "brn", "gry", "grn", "hzl", "oth"]

def validate_pid(pid: str):
    return pid_re.match(pid)

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

passports = read_passports()

count_valids = 0
for passport in passports:
    is_valid = True
    for required_field in required_fields:
        if not passport.get(required_field):
            is_valid = False
    if is_valid:
        is_valid = is_valid and validate_byr(passport["byr"])
        is_valid = is_valid and validate_iyr(passport["iyr"])
        is_valid = is_valid and validate_eyr(passport["eyr"])
        is_valid = is_valid and validate_hgt(passport["hgt"])
        is_valid = is_valid and validate_hcl(passport["hcl"])
        is_valid = is_valid and validate_ecl(passport["ecl"])
        is_valid = is_valid and validate_pid(passport["pid"])
    if is_valid:
        count_valids = count_valids + 1

print(count_valids)