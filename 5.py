# have at least 3 vovewls  
def vovewls(s):
    c = 0
    for x in s:
        if x in ['a', 'e', 'i', 'o', 'u']:
            c += 1
    return c >= 3

# at least one doubled character 
def double(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False

# do not contain forbiden strings 
def forbiden(s):
    for x in ["ab", "cd", "pq", "xy"]:
        if x in s:
            return False
    return True

c = 0
for line in open("input5.txt"):
    if vovewls(line) and double(line) and forbiden(line):
        c += 1

print(c)
