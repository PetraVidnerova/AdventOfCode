import numpy as np
size = 1000000
sums = np.zeros(size)

for i in range(1, size):
    print("->", i)
    x = i
    for j in range(50):
        if x >= size:
            break
        sums[x] += 11 * i
        if sums[x] >= 34000000:
            print("***********************************", x)
            quit()
        x += i
