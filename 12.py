
def count(line):
    number = 0
    sum = 0
    negative = False
    for c in line:
        if c == '-':
            negative = True
            continue
        if c.isdigit():
            number = number * 10 + ord(c) - ord('0')
            continue
        if negative:
            sum -= number
        else:
            sum += number
        number = 0
        negative = False
    return sum

sum = 0
for line in open("input12.txt"):
    sum += count(line)

print(sum)
