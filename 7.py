import re

f = open("input7b.txt")

dict = {}


def split(s):
    (left, right) = re.findall("(.*) -> ([a-z]*)", s)[0]
    return (left, right)


def insert(left, right):
    if left.isdigit():
        dict[right] = int(left)
        return True
    elif left in dict:
        dict[right] = dict[left]
        return True
    return False


def doand(a, b, right):
    if a.isdigit() and b in dict:
        dict[right] = (int(a) & dict[b]) & 0xffff
        return True
    if a in dict and b.isdigit():
        dict[right] = (int(b) & dict[a]) & 0xffff
        return True
    if a in dict and b in dict:
        dict[right] = dict[a] & dict[b]
        return True
    else:
        return False


def door(a, b, right):
    if a in dict and b in dict:
        dict[right] = dict[a] | dict[b]
        return True
    else:
        return False


def donot(a, right):
    if a in dict:
        dict[right] = (~dict[a]) & 0xffff
        return True
    else:
        return False


def dolshift(a, b, right):
    if a in dict:
        dict[right] = dict[a] << int(b)
        return True
    else:
        return False


def dorshift(a, b, right):
    if a in dict:
        dict[right] = dict[a] >> int(b)
        return True
    else:
        return False


def evaluate(line):
    # evaluates one line
    # returns true if the line was evaluated
    # or false if arguments not yet in dictionary
    # result in global dict
    (left, right) = split(line)
    print(left, right)

    if "AND" in left:
        (a, b) = re.findall("([a-z0-9]*) AND ([0-9a-z]*)", left)[0]
        return doand(a, b, right)

    if "OR" in left:
        (a, b) = re.findall("([a-z0-9]*) OR ([0-9a-z]*)", left)[0]
        return door(a, b, right)

    if "NOT" in left:
        a = re.findall("NOT ([a-z]*)", left)[0]
        return donot(a, right)

    if "RSHIFT" in left:
        (a, b) = re.findall("([a-z]*) RSHIFT ([0-9]*)", left)[0]
        return dorshift(a, b, right)

    if "LSHIFT" in left:
        (a, b) = re.findall("([a-z]*) LSHIFT ([0-9]*)", left)[0]
        return dolshift(a, b, right)

    # no keyword , asignment
    return insert(left, right)


def go(list):
    # go throught list and evaluates all possible lines
    # returns list of not evaluated lines
    unsuccess = []
    for line in list:
        if evaluate(line):
            continue
        else:
            unsuccess.append(line)
    return unsuccess

list = []
for line in f:
    list.append(line)

while list:
    list = go(list)

print(dict['a'])
