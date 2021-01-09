# 모의고사

# 내 풀이
def solution(answers):
    answer = []
    nums = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    ]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(len(nums)):
            if answers[i] == nums[j][i%len(nums[j])]: cnt[j] += 1
    max_cnt = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == max_cnt: answer.append(i+1)
    return answer
print(solution([1,2,3,4,5]))


# 남의 풀이
# def solution(answers):
#     nums = [
#         [1, 2, 3, 4, 5], 
#         [2, 1, 2, 3, 2, 4, 2, 5], 
#         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
#     ]
#     score = [0] * len(nums) # [0,0,0] 대신 * 로 처리
#     result = []

#     for idx, answer in enumerate(answers): #enumerate = 값고 인덱스 값이 같이 필요할 때 사용하는 함수
#         if answer == nums[0][idx%len(nums[0])]:
#             score[0] += 1
#         if answer == nums[1][idx%len(nums[1])]:
#             score[1] += 1
#         if answer == nums[2][idx%len(nums[2])]:
#             score[2] += 1

#     for idx, s in enumerate(score): 
#         if s == max(score):
#             result.append(idx+1)
#     return result
# print(solution([1,2,3,4,5]))