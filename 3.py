def move(c, x, y):
    """
    Returns new position after move 'c'.
    Adds the position to list. 
    """
    global l

    if (c == ">"):
        x += 1
    elif (c == "<"):
        x -= 1
    elif (c == "^"):
        y += 1
    elif (c == "v"):
        y -= 1

    if (x, y) not in l:
        l.append((x, y))
    return (x, y)


s = open("input3.txt").read()

(x, y) = (0, 0)
(a, b) = (x, y)
l = [(x, y)]

# len(s) is even
i = 0
while i < len(s) - 1:
    (x, y) = move(s[i], x, y)
    (a, b) = move(s[i + 1], a, b)
    i += 2

print(l)
print(len(l))
