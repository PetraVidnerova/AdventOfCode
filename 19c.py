rules = []
start = "e"
target_output = ""
solitary_atoms = set([])


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


def split_atoms(molecule):
    atoms = set([])
    i = 0
    while (i < len(molecule)):
        name = molecule[i]
        if i + 1 < len(molecule) and molecule[i + 1].islower():
            name = name + molecule[i + 1]
            atoms.add(name)
            i += 2
        else:
            atoms.add(name)
            i += 1
    return atoms


def get_solitary_atoms():
    global rules
    atoms = set([])
    for molecule in [x[0] for x in rules] + [x[1] for x in rules]:
        for atom in split_atoms(molecule):
            atoms.add(atom)
    # Check if atom is solitary = only on right side of rules.
    nonsolitary = set([])
    print(atoms)
    for a in atoms:
        for r in rules:
            if a not in r:
                continue
            nonsolitary.add(a)
    atoms = atoms - nonsolitary
    return atoms


def preprocess():
    # Apply rules with solitary atoms and remove them from rules.
    global solitary_atoms
    global rules
    global target_output

    pre_rules = set([])
    for r in rules:
        for a in solitary_atoms:
            if a in r[1]:
                pre_rules.add(r)
    for r in pre_rules:
        target_output = target_output.replace(r[1], r[0])
        rules.remove(r)


init()
solitary_atoms = get_solitary_atoms()
print(target_output)
preprocess()
print(len(rules))
print(target_output)
