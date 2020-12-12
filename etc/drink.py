n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


#dfs
def dfs(graph, x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x+1, y)
        dfs(graph, x-1, y)
        dfs(graph, x, y+1)
        dfs(graph, x, y-1)
        return True # 0인거 다 돌고 왔으면 True 넘기기
    return False # 0인게 없으면 False 넘기기


count = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j): 
            count += 1

print(count)     
