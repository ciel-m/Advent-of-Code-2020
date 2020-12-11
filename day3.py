f = open('input3.txt', 'r')
mapping = [x.strip() for x in f]
row, col = 0, 0
trees = 0
while row < len(mapping):
    if mapping[row][col] == "#":
        trees += 1
    #slope of 3, 1
    row += 1
    col += 3
    if col >= len(mapping[0]):
        col %= len(mapping[0])
    print(col)
print("trees: ", trees)