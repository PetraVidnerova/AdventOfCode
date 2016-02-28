import re
import itertools

cities = []
distances = {}

f = open("input9a.txt")

for line in f:
    (city1, city2, dist) = re.findall("(.*) to (.*) = (.*)", line)[0]
    if city1 not in cities:
        cities.append(city1)
    if city2 not in cities:
        cities.append(city2)
    distances[(city1, city2)] = int(dist)

print(cities)
print(distances)


def distance(road):
    sum = 0
    for i in range(0, len(road) - 1):
        if (road[i], road[i + 1]) in distances:
            sum += distances[(road[i], road[i + 1])]
        else:
            sum += distances[(road[i + 1], road[i])]
    return sum

#print(min(map(distance, itertools.permutations(cities))))
print(max(map(distance, itertools.permutations(cities))))
