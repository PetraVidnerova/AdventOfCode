s = open("input1.txt", "r").read()

floor = 0
pos = 0
for x in s:
    if floor < 0:
        break
    pos += 1
    if (x == "("):
        floor += 1
        continue
    if (x == ")"):
        floor -= 1
        continue

print(pos)
