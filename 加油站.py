## leetcode https://leetcode-cn.com/problems/gas-station/solution/134-jia-you-zhan-tan-xin-jing-dian-ti-mu-xiang-jie/

def func(gas,cost):
    start = 0
    curSum = 0
    totalSum = 0
    for i in range(len(gas)):
        curSum += gas[i] - cost[i]
        totalSum += gas[i] - cost[i]
        if curSum <0:
            curSum = 0
            start = i+1
    if totalSum <0:
        return -1
    return start

# g = [1,2,3,4,5]
# c = [3,4,5,1,2]
g = [2,3,4]
c = [3,4,3]
print(func(g,c))



















# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         start = 0
#         curSum = 0
#         totalSum = 0
#         for i in range(len(gas)):
#             curSum += gas[i] - cost[i]
#             totalSum += gas[i] - cost[i]
#             if curSum < 0:
#                 curSum = 0
#                 start = i + 1
#         if totalSum < 0: return -1
#         return start