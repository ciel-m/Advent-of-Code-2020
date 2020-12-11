def check(field, val):
    if field == "byr":
        return 1920 <= int(val) <= 2002
    elif field == "iyr":
        return 2010 <= int(val) <= 2020
    elif field == "eyr":
        return 2020 <= int(val) <= 2030
    elif field == "hgt":
        if val[-2:] == "cm":
            return 150 <= int(val[:-2]) <= 193
        elif val[-2:] == "in":
            return 59 <= int(val[:-2]) <= 76
        else:
            return False
    elif field == "hcl":
        allowed = "0123456789abcdef"
        return val[0] == "#" and all([c in allowed for c in val[1:]]) and len(val[1:]) == 6
    elif field == "ecl":
        return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return val.isnumeric() and len(val) == 9
    elif field == "cid":
        return True
    else:
        return False

f = open("input4.txt","r")
passports = []
curr = ""
for line in f:
    curr += line.strip() + " "
    if line == "\n":
        if curr:
            passports.append(curr.strip())
        curr = ""
valid = 0
for p in passports:
    currPassport = p.split()
    fieldval = [f.split(":") for f in currPassport]
    print(fieldval)
    if all([check(x[0], x[1]) for x in fieldval]) and ("byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p):
        print("True")
        valid +=1
    else: print(len(fieldval))
print(valid)