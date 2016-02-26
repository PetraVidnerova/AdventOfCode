
s = open("input1.txt", "r").read()

floor = 0
for x in s:
    if (x == "("):
        floor += 1
        continue
    if (x == ")"):
        floor -= 1
        continue

print(floor)
