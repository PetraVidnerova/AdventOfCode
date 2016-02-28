import itertools

cookbook = {}


def readline(line):
    global cookbook
    words = line.split()
    cookbook[words[0]] = [int(words[2].replace(",", "")), int(words[4].replace(",", "")),
                          int(words[6].replace(",", "")), int(words[8].replace(",", ""))]


def score(list):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for item in list:
        capacity += cookbook[item][0]
        durability += cookbook[item][1]
        flavor += cookbook[item][2]
        texture += cookbook[item][3]
    return max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)

for line in open("input15.txt"):
    readline(line)

print(cookbook)

mx = None
for x in itertools.combinations_with_replacement(cookbook.keys(), 100):
    scr = score(x)
    if mx is None or scr > mx:
        mx = scr

print(mx)
