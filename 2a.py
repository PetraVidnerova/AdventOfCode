ribbon = 0
for line in open("input2.txt"):
    lengths = sorted(map(int, line.split("x")))

    ribbon += 2 * lengths[0] + 2 * lengths[1]
    ribbon += lengths[0] * lengths[1] * lengths[2]

print(ribbon)
