# 네트워크

def dfs(i, n, computers):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and visited[j] != True:
            dfs(j, n, computers)


def solution(n, computers):
    answer = 0

    for i in range(n):
        if visited[i] == False:
            answer += 1
            dfs(i, n , computers)

    return answer


visited = [False] * 3
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))