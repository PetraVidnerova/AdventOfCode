rules = []
start = "e"
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
            rules.append((words[0], words[2]))
        else:
            target_output = line.strip()


def get_next_atom(s):
    if len(s) == 0:
        return None
    if len(s) == 1:
        return s
    ret = s[0]
    if s[1].islower():
        ret += s[1]
    return ret


init()
print(rules)
print(target_output)

working_list = []
while True:
    atom = get_next_atom(target_output)
    if not atom:
        break
    working_list.append(atom)
    target_output = target_output[len(atom):]
print(working_list)

total = len(working_list)
Rn_count = 0
Y_count = 0
for atom in working_list:
    if atom == "Rn":
        Rn_count += 1
    if atom == "Ar":
        Rn_count += 1
    if atom == "Y":
        Y_count += 1

print(total - Rn_count - 2 * Y_count - 1)
