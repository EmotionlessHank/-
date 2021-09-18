import random

def random1000():
    res = ''
    t = -1
    while t<0 or t>1000:
        for i in range(10):
            res += str(random.randint(0,1))
        t = int(res,2)
    return t

print(random1000())