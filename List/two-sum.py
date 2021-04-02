def solution(nums, target):
    answer = []
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                answer.append([i, j])

    return answer

print(solution([2, 7, 11, 15], 9))