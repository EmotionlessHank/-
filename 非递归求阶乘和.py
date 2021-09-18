def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n = int(input())
s = 1
for i in range(2,n+1):
    s += fact(i)
print(s)