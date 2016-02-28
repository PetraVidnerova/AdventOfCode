import itertools

weights = []
for line in open("input24a.txt"):
    weights.append(int(line))

required_weight = sum(weights) / 3
print(required_weight)

# start with highest value
weights = weights[::-1]


def next_solution(solution):
    i = 0
    while solution[i] + 1 == 3:
        solution[i] = 0
        i += 1
        if i >= len(solution):
            solution.append(0)
            break
    solution[i] += 1
    return solution


def check_solution(weights, solution, required):
    sums = [0, 0, 0]
    for i in range(len(solution)):
        sums[solution[i]] += weights[i]
    for i in range(3):
        if not sums[i] == required:
            return False
    return True


def print_solution(weights, sol):
    quantum = 0
    for group in range(3):
        print("[", end="")
        if group == 0:
            quantum = 1
        for i in range(len(solution)):
            if solution[i] == group:
                if group == 0:
                    quantum *= weights[i]
                print(weights[i], end="")
        print("]", end="")
    print(" ", quantum)


#input("-- press something --")
solution = [0] * len(weights)
while len(solution) == len(weights):
    if check_solution(weights, solution, required_weight):
        print_solution(weights, solution)
    solution = next_solution(solution)
