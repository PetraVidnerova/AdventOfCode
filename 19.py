rules = []
rulesPart = True
start = ""
for line in open("input19.txt"):
    if not line.strip():
        rulesPart = False
        continue
    if rulesPart:
        words = line.split()
        rules.append((words[0], words[2]))
    else:
        start = line


def replaceall(target, new, s):
    # for each occurence of target replace it
    # return list of result
    words = s.split(target)
    res = []
    for n in range(len(words) - 1):
        result = ""
        for i in range(len(words) - 1):
            result += words[i]
            if i == n:
                result += new
            else:
                result += target
        result += words[len(words) - 1]
        res.append(result)
    return res

print(start)
print(rules)

newstrings = []
for (key, newstring) in rules:
    strings = replaceall(key, newstring, start)
    for s in strings:
        if s not in newstrings:
            newstrings.append(s)

print(newstrings)
print(len(newstrings))
