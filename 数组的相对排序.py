# leetcode https://leetcode-cn.com/problems/relative-sort-array/

def func(l1,l2):
    if not l2:
        return l1
    if not l1:
        return l2
    res = []
    tmp = []
    for i in l2:
        # res.append(i)
        if i in l1:
            t = [i for _ in range(l1.count(i))]
            res += t
            while i in l1:
                l1.remove(i)
    return res+l1

print(func([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))
