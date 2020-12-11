f = open('input3.txt', 'r')
mapping = [x.strip() for x in f]
def slide(run, rise):
    row, col = 0, 0
    trees = 0
    while row < len(mapping):
        if mapping[row][col] == "#":
            trees += 1
        row += rise
        col += run
        if col >= len(mapping[0]):
            col %= len(mapping[0])
    return trees
print(slide(1,1)*slide(3,1)*slide(5,1)*slide(7,1)*slide(1,2))