def solution(nums):
    nums.sort()
    res = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            res += nums[i]
    return res

print(solution([1,4,3,2]))
