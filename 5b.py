
def rule1(s):
    """
    It contains a pair of any two letters that appears 
    at least twice in the string without overlapping, 
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa.
    """
    i = 0
    while i < len(s) - 4:
        pair = s[i] + s[i + 1]
        if pair in s[i + 2:]:
            return True
        i += 1
    return False


def rule2(s):
    """
    It contains at least one letter which repeats with exactly one
    letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    i = 0
    while i < len(s) - 2:
        if s[i] == s[i + 2]:
            return True
        i += 1
    return False

c = 0
for line in open("input5.txt"):
    print(line)
    if rule1(line) and rule2(line):
        c += 1

print(c)
