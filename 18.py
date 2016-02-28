import numpy as np

lights = np.zeros((102, 102))


def switch_on_corners():
    global lights
    lights[1, 1] = 1
    lights[1, 100] = 1
    lights[100, 1] = 1
    lights[100, 100] = 1


def count(x, y):
    global lights
    count = 0
    for i in range(x - 1, x + 2):
        if lights[i, y - 1] == 1:
            count += 1
        if lights[i, y + 1] == 1:
            count += 1
    if lights[x - 1, y] == 1.0:
        count += 1
    if lights[x + 1, y] == 1.0:
        count += 1
    return count


def evolve():
    global lights
    newgrid = np.zeros((102, 102))

    for x in range(1, 101):
        for y in range(1, 101):
            neighbors = count(x, y)
            if lights[x, y] == 1.0 and (neighbors == 2 or neighbors == 3):
                newgrid[x, y] = 1
            elif lights[x, y] == 0.0 and neighbors == 3:
                newgrid[x, y] = 1
    lights = newgrid
# uncomment for second part
    switch_on_corners()


y = 1
for line in open("input18.txt"):
    x = 1
    for c in line:
        if c == '#':
            lights[x, y] = 1
        x += 1
    y += 1
switch_on_corners()


for i in range(100):
    evolve()


print(sum(sum(lights)))
