import itertools

points = {}
people = []


def eatline(line):
    global people
    global points

    words = line.split()
    if words[0] not in people:
        people.append(words[0])
    gain = int(words[3])
    if words[2] == "lose":
        gain = -1 * gain
    points[(words[0], words[10].replace(".", ""))] = gain


def happyness(table):
    cost = 0
    cost += points[(table[0], table[len(table) - 1])]
    cost += points[(table[len(table) - 1], table[0])]
    for i in range(len(table) - 1):
        cost += points[(table[i], table[i + 1])]
        cost += points[(table[i + 1], table[i])]
    return cost

for line in open("input13.txt"):
    eatline(line)

print(points)

max = None
list = []
for table in itertools.permutations(people):
    h = happyness(table)
    if max is None or h > max:
        max = h
        list = table

print(max)
