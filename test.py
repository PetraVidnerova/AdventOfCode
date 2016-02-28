import itertools

weights = []
for line in open("input24.txt"):
    weights.append(int(line))

required_weight = sum(weights) / 4
print(required_weight)

# start with highest value
weights = weights[::-1]


def product(x):
    res = 1
    for i in x:
        res *= i
    return res


def check(weights, required_weight, number):
    for i in range(10):
        for x in itertools.combinations(weights, i):
            if sum(x) == required_weight and (number == 2 or check([a for a in weights if a not in x], required_weight, number - 1)):
                return True
    return False

min = None
for i in range(10):
    for x in itertools.combinations(weights, i):
        if sum(x) == required_weight and check([a for a in weights if a not in x], required_weight, 3):
            p = product(x)
            if min == None or p < min:
                min = p
            print(x, p)

print("-->", min)
