f = open("input8.txt")


def count(line):
    sum = 0
    i = 0
    while i < len(line):
        if line[i] == '"':
            sum += 1
            i += 1
            continue
        if line[i] == '\\':
            if line[i + 1] == '"' or line[i + 1] == "\\":
                sum += 1
                i += 2
                continue
            if line[i + 1] == 'x':
                sum += 3
                i += 4
                continue
        i += 1
    return sum

sum = 0
for line in f:
    sum += count(line)


print(sum)
