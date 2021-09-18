# leetcode https://leetcode-cn.com/problems/longest-common-prefix/

def maxPre(l):
    # 利用字典排序，最大和最小，直接比较两者即可
    m = max(l)
    n = min(l)
    for i in range(len(n)):
        if n[i] != m[i]:
            return n[0:i]
    return n


print(maxPre(["dog", "racecar", "car"]))
