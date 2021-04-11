
# 부르트 포스로 계산

def solution1(nums, target):
    answer = []
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                answer.append([i, j])

    return answer

print(solution1([2, 7, 11, 15], 9))

# in을 이용한 탐색

def solution2(nums, target):
    answer = []
    length = len(nums)
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)

    return answer

# 첫 번째 수를 뺀 결과 키 조회

def solution3(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]
