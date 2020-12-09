# 타겟 넘버

def dfs(numbers, i, sum, target):
    if sum == target and i == len(numbers):
        return 1    #global 변수 없이 값 리턴으로 처리 가능
    if i == len(numbers): # i ==len(numbers) and sum >= target으로 두면 -처리 후 타겟과 같을 경우 누락됨
        return 0
    return dfs(numbers, i+1, sum+numbers[i], target) + dfs(numbers, i+1, sum-numbers[i], target)

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

print(solution([1,1,1,1,1], 3))