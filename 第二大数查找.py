def func(nums):
    if len(nums) == 2:
        return nums[-2]
    for i in range(len(nums)-1):
        if i ==2:
            break
        for j in range(len(nums)-i-1):
            if nums[j+1] < nums[j]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums[-2]

l = [2,4,6,8,8,10]
print(func(l))