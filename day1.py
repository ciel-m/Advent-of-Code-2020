f = open("./input.txt", "r")
l = []
for eachLine in f:
    l.append(int(eachLine))
# part 1
def twosum(target, arr):
    result = 0
    for eachNum in arr:
        res = target - eachNum
        if res in arr:
            result = res * eachNum
    return result
# part 2, implemented 3sum using 2sum
for i in range(len(l)):
    ret = l[i] * twosum(2020 - l[i], l[i+1:])
    if ret: print(ret)
