f = open("./input2.txt", "r")
parsed = [x.split() for x in f]
#part one
def partone():
    count = 0
    for p in parsed:
        limits = p[0].split("-")
        mini, maxi = int(limits[0]), int(limits[1])
        if mini <= p[2].count(p[1][0]) <= maxi:
            count += 1
    print(count)
# part two
def parttwo():
    count = 0
    for p in parsed:
        indexes = [int(x)-1 for x in p[0].split("-")]
        char = p[1][0]
        print(indexes, char)
        #xor
        if (char == p[2][indexes[0]]) ^ (char == p[2][indexes[1]]):
            count += 1
    print(count)
# partone()
parttwo()