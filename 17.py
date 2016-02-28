import itertools

buckets = []
for line in open("input17.txt"):
    buckets.append(int(line))

count = 0
min = None
combinations = []
for size in range(1, len(buckets)):
    for subset in itertools.combinations(buckets, size):
        if sum(subset) == 150:
            print(subset)
            count += 1
            combinations.append(subset)
            if min == None or len(subset) < min:
                min = len(subset)

print("All combinations", count)
count = 0
for subset in combinations:
    if len(subset) == min:
        count += 1
print("Minimal combinations", count)
