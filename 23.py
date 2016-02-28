def read_line():
    words = line.split()
    if words[1] == 'a' or words[1] == 'a,':
        reg = 0
    elif words[1] == 'b' or words[1] == 'b,':
        reg = 1
    else:
        reg = int(words[1])

    if words[0] in ['hlf', 'tpl', 'inc', 'jmp']:
        return (words[0], reg)
    else:
        return (words[0], reg, int(words[2]))


registers = [1, 0]


def exec(instr):
    global registers
    if instr[0] == "inc":
        registers[instr[1]] += 1
        return 1
    elif instr[0] == "hlf":
        registers[instr[1]] = int(registers[instr[1]] / 2)
        return 1
    elif instr[0] == "tpl":
        registers[instr[1]] *= 3
        return 1
    elif instr[0] == "jmp":
        return int(instr[1])
    elif instr[0] == "jie":
        if registers[instr[1]] % 2 == 0:
            return instr[2]
        else:
            return 1
    elif instr[0] == "jio":
        if registers[instr[1]] == 1:
            return instr[2]
        else:
            return 1


program = []
for line in open("input23.txt"):
    program.append(read_line())

i = 0
while i < len(program):
    print(i, program[i], registers)
    i += exec(program[i])


print(registers[1])
