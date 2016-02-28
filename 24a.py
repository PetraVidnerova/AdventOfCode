import itertools

weights = []
for line in open("input24a.txt"):
    weights.append(int(line))

required_weight = sum(weights)
print(required_weight)

# start with highest value
weights = weights[::-1]


def checksolution(groups, sizes):
    for i in range(3):
        if not groups[i] == sizes[i]:
            return False
    return True


def split(weights, sizes, groups):
    """
    Split items from 'list' into groups.
    Sizes of groups are given in 'sizes'.
    Returns groups  if split is possible, 
    else empty list.
    """
    for i in range(3):
        if i > 0:
            groups[i - 1].remove(list[0])
        groups[i].append(weights[0])
        newsizes = sizes
        newsizes[i] -= weights[0]
        groups = split(weights[1:], newsizes, groups)
        if groups != [] and checksolution(groups, sizes):
            return groups
        else:
            return []
    return []


groups = [[], [], []]
split(weights, 520, 520, 520, groups)[0]
