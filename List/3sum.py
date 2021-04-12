import collections as c

def solution(nums):
    minus, plus, zero = c.defaultdict(int), c.defaultdict(int), c.defaultdict(int)
    
    answer = []

    for num in nums:
        if num < 0:
            minus[num] += 1
        elif num > 0:
            plus[num] +=1
        else:
            zero[num] += 1

    if zero.get(0) is not None:
        if zero[0] >= 3:
            answer.append([0, 0, 0])

        for num in minus:
            if plus.get(abs(num)) is not None:
                answer.append([0, num, num*(-1)])

    plus_list = list(plus.keys())
    minus_list = list(minus.keys())

    for i in range(len(plus_list)):
        if plus[plus_list[i]] > 1 and minus.get(plus_list[i]*(-2)) is not None:
            answer.append([plus_list[i], plus_list[i], plus_list[i]*(-2)])

    for i in range(len(plus_list)-1):
        for j in range(i+1, len(plus_list)):
            key = plus_list[i] + plus_list[j]
            if minus.get(key*(-1)) is not None:
                answer.append([plus_list[i], plus_list[j], key*(-1)])

    for i in range(len(minus_list)):
        if minus[minus_list[i]] > 1 and plus.get(minus_list[i]*(-2)) is not None:
            answer.append([minus_list[i], minus_list[i], minus_list[i]*(-2)])

    for i in range(len(minus_list)-1):
        for j in range(i+1, len(minus_list)):
            key = minus_list[i] + minus_list[j]
            if plus.get(abs(key)) is not None:
                answer.append([minus_list[i], minus_list[j], abs(key)])

    return answer


print(solution([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
