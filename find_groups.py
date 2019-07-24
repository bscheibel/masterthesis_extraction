from itertools import combinations, product
def canMerge (g, h):
    for i, j in g:
        for x, y in h:
            if abs(i - x) <= 1 and abs(j - y) <= 1:
                return True
    return False

def findGroups (field):
    # initialize one-element groups
    groups = [[(i, j)] for i, j in product(range(len(field)), range(len(field[0]))) if field[i][j] != '  ']

    # keep joining until no more joins can be executed
    merged = True
    while merged:
        merged = False
        for g, h in combinations(groups, 2):
            if canMerge(g, h):
                g.extend(h)
                groups.remove(h)
                merged = True
                break

    return groups

# intialize field
field = "drawings/5129275_Rev01-GV12.txt"
groups = findGroups(field)

print((groups)) # 3