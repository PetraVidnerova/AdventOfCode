import re
import numpy as np

f = open("input6.txt")

lights = np.zeros((1000, 1000))
for line in f:
    what = re.findall("([^0-9]*)", line)[0]
    numbers = re.findall("([0-9]*),", line)
    xstart = int(numbers[0])
    xend = int(numbers[1]) + 1
    numbers = re.findall(",([0-9]*)", line)
    ystart = int(numbers[0])
    yend = int(numbers[1]) + 1
    print(what)
    for x in range(xstart, xend):
        for y in range(ystart, yend):
            if (what == "turn on "):
                lights[x, y] += 1
                continue
            if (what == "toggle "):
                lights[x, y] += 2
                continue
            if (what == "turn off "):
                lights[x, y] = max(0, lights[x, y] - 1)
                continue
# print(lights)
print(sum(sum(lights)))
