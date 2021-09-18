def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
s = 0
def sumFact(m):
    res = 0
    if m == 1:
        return 1
    elif m == 0:
        return 0
    else:
        res = sumFact(m-1)+fact(m)
    return res


print(sumFact(10))