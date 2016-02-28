import itertools

sizes = []
for line in open("input24.txt"):
    sizes.append(int(line))

size = sum(sizes) / 3

print(size)
