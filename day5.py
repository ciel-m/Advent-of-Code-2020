f = open("input5.txt", "r")
def findRow(s):
    hi, lo = 127, 0
    for eachChar in s[:-1]:
        if eachChar == "F":
            hi = (lo + hi) // 2
        else:
            lo = (lo + hi) // 2 + 1
    return hi if s[-1] == "B" else lo

def findCol(s):

    hi, lo = 7, 0
    for eachChar in s[:-1]:
        if eachChar == "L":
            hi = (lo + hi) // 2
        else:
            lo = (lo + hi) // 2 + 1
    return hi if s[-1] == "R" else lo

def findSeatId(s):
    row = s[:7]
    col = s[7:]
    return findRow(row) * 8 + findCol(col)

print(max([findSeatId(x.strip()) for x in f]))