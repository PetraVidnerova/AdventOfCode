import itertools

weights = []
for line in open("input24.txt"):
    weights.append(int(line))
weights = weights[::-1]

required_weight = sum(weights) / 3
print(required_weight)

print(len(weights))
print(weights)

for x in itertools.permutations(weights):
    print(".")
