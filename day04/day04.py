import re
with open("input.txt") as f:
    passports = [line.replace("\n", " ").strip() for line in f.read().split("\n\n")]
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    valid2 = 0
    for line in passports:
        d = dict(item.split(":") for item in line.split(" "))
        if all(key in d for key in keys):
            valid += 1
            if 1920 <= int(d['byr']) <= 2002 and \
                2010 <= int(d['iyr']) <= 2020 and \
                2020 <= int(d['eyr']) <= 2030 and \
                re.match(r'^\d+..', d['hgt']) and \
                ((d['hgt'].endswith('cm') and 150 <= int(d['hgt'][:-2]) <= 193) or (d['hgt'].endswith('in') and 59 <= int(d['hgt'][:-2]) <= 76)) and \
                re.match(r'^#[\da-f]{6}$', d['hcl']) and \
                d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
                re.match(r'^\d{9}$', d['pid']):
                    valid2 += 1
    print(valid, valid2)
