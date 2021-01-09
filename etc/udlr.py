# 상하좌우 문제

# 내 풀이
n = int(input())
list = input().split()
point = [1, 1]

for ch in list:
    if ch == 'R':
        if point[1] >= n: continue
        else: point[1] +=1
    elif ch == 'L':
        if point[1] <= 1: continue
        else: point[1] -=1
    elif ch == 'U':
        if point[0] <= 1: continue
        else: point[0] -=1
    elif ch == 'D':
        if point[0] >= n: continue
        else: point[0] +=1
print(point) # 최종 위치

######
# 남의 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    # 공간을 벗어나는 경우 무시
    if nx <1 or ny <1 or nx >n or ny > n:
        continue
    x, y = nx, ny
print(x, y) # 최종 위치
