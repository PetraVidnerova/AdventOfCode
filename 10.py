
def read(input):
    # one iteration of read
    input = input + "x"  # last char is ignored
    result = ""
    lastchar = None
    count = 0
    for ch in input:
        if ch == lastchar:
            count += 1
            continue
        if lastchar:
            result = result + str(count) + str(lastchar)
        count = 1
        lastchar = ch
    return result


input = "3113322113"
for x in range(50):
    print(x)
    input = read(input)

print(len(input))
