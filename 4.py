import hashlib

input = "ckczppom"


def getmd5(k):
    m = hashlib.md5()
    m.update(k.encode())
    return m.hexdigest()

for x in range(1000000, 10000000):
    key = input + str(x)
    if getmd5(key).startswith("000000"):
        print(x)
        break
        
