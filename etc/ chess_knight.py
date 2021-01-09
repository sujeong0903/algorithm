#왕실의 나이트

# 수평으로 두 칸 이동한 뒤 수직으로 한 칸 이동
# 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동

data = input()
x , y = (ord(data[0]) - ord('a') + 1), int(data[1])
cnt = 0
# 이동하는 방향은 리스트에 넣기 #튜플은 이미 생성된 원소를 제거하거나, 변경할 수 없음. 튜플은 동일한 원소 타입일 때 사용
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2),(1, 2)] 
for step in steps:
    dx = x + step[0]
    dy = y + step[1]
    if dx > 0 and dx <= 8 and dy > 0 and dy <= 8: cnt += 1 
print(cnt)

