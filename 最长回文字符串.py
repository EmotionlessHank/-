# leetcode https://leetcode-cn.com/problems/longest-palindromic-substring/solution/dong-tai-gui-hua-ni-chao-rong-yi-li-jie-j8frz/

def func(s):
    length = len(s)
    start,maxLen = 0,1
    dp = [[False]*length for _ in range(length)]

    if length < 2:
        return s

    # base case
    for i in range(length):
        dp[i][i] = True

    # 终点
    for j in range(1,length):
        # 起点
        for i in range(0,j):
            if s[i] == s[j]:
                if j-i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            if dp[i][j]:
                if j-i+1 > maxLen:
                    maxLen = j-i+1
                    start = i
    return s[start:start+maxLen]

nums = "babad"
print(func(nums))



