import json


def read_list(list):
    sum = 0
    for i in list:
        if type(i) == int:
            sum += i
        else:
            sum += read_json(i)
    return sum


def read_dictionary(dict):
    sum = 0
    for i in dict.values():
        if type(i) == int:
            sum += i
            continue
        elif type(i) == str:
            if i == "red":
                return 0
        else:
            sum += read_json(i)
    return sum


def read_json(json):
    if type(json) == list:
        return read_list(json)
    elif type(json) == dict:
        return read_dictionary(json)
    else:
        if not type(json) == str:
            raise Exception()
    return 0

json = json.loads(open("input12.txt").read())

print(read_json(json))
