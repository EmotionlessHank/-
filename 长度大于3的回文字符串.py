def func(s:str):
    l = len(s)
    res = []
    for j in range(2,l):
        for i in range(0,j):
            if j-i + 1<3:
                continue
            if s[i:j+1] == s[i:j+1][::-1]:
                res.append(s[i:j+1])
    return res

s = 'abaabbaabababa'
print(list(set(func(s))))


