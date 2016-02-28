import queue

rules = []
target_output = ""


def init():
    global rules
    global target_output
    rulesPart = True
    for line in open("input19.txt"):
        if not line.strip():
            rulesPart = False
            continue
        if rulesPart:
            words = line.split()
            rules.append((words[2], words[0]))
        else:
            target_output = line.strip()


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


init()
print(rules)
print(target_output)

q = queue.PriorityQueue()
q.put((len(target_output), 0, target_output))
history = set([])
while True:
    length, iteration, molecule = q.get()
    print(length, iteration, molecule)
    if molecule == 'e':
        print("-->", iteration)
        break
    # to prevent cycles
    if molecule in history:
        continue
    else:
        history.add(molecule)

    for r in rules:
        for s in replaceall(r[0], r[1], molecule):
            q.put((len(s), iteration + 1, s))
