
def increase(passwd):
    increase = True
    newpasswd = ""
    for c in reversed(passwd):
        if increase:
            if c == 'z':
                newpasswd += 'a'
                continue
            else:
                newpasswd += chr(ord(c) + 1)
                increase = False
        else:
            newpasswd += c
    return newpasswd[::-1]


def checkStraight(passwd):
    for i in range(len(passwd) - 2):
        if ord(passwd[i + 1]) == ord(passwd[i]) + 1 and ord(passwd[i + 2]) == ord(passwd[i]) + 2:
            return True
    return False


def noIOL(passwd):
    if 'i' in passwd or 'o' in passwd or 'l' in passwd:
        return False
    return True


def checkpair(passwd):
    i = 0
    pairs = 0
    while i < len(passwd) - 1:
        if passwd[i] == passwd[i + 1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs >= 2

#pwd = increase("hxbxwxba")
pwd = increase("hxbxxyzz")
while not(checkpair(pwd) and noIOL(pwd) and checkStraight(pwd)):
    pwd = increase(pwd)

print(pwd)
