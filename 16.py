
wanted = {"children": 3,  "samoyeds": 2,  "akitas": 0, "vizslas": 0,   "cars": 2,
          "perfumes": 1}
upper_bound = {"pomeranians": 3, "goldfish": 5}
lower_bound = {"cats": 7, "trees": 3}


def readSue(line):
    words = line.split()
    i = 2
    while i < len(words):
        words[i] = words[i].replace(':', '')
        words[i + 1] = words[i + 1].replace(',', '')
        if words[i] in wanted and wanted[words[i]] != int(words[i + 1]):
            return
        if words[i] in upper_bound and upper_bound[words[i]] <= int(words[i + 1]):
            return
        if words[i] in lower_bound and lower_bound[words[i]] >= int(words[i + 1]):
            return
        i += 2
    print(words[0], words[1])


for line in open("input16.txt"):
    readSue(line)
