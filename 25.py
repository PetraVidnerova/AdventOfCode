start = 20151125


def get_next(number):
    return (number * 252533) % 33554393

start_i = 1


def get_next_coord(i, j):
    global start_i

    if i == 1:
        i = start_i + 1
        start_i += 1
        j = 1
        return (i, j)
    return (i - 1, j + 1)

index = 1
(i, j) = (1, 1)
number = start
while (i, j) != (2978, 3083):
    (i, j) = get_next_coord(i, j)
    number = get_next(number)


print(number)
