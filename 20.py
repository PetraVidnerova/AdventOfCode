import numpy as np

sums = np.zeros(1000000)

for i in range(1, 1000000):
    print("->", i)
    x = i
    while (x < 1000000):
        sums[x] += 10 * i
        if sums[x] > 34000000:
            print("***********************************", x)
            quit()
        x += i
