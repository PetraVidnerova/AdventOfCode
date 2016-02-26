sum = 0
for line in open("input2.txt"):
    (l, w, h) = map(int, line.split("x"))

    sum += 2 * l * w + 2 * w * h + 2 * l * h
    sum += min([l * w, w * h, l * h])

print(sum)
