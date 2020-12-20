# 모험가 길드

# n = 5
# data = [2, 3, 1, 2, 2]
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
cnt = 0
#작은 수끼리 모으는게 큰 수를 모으는 것 보다 효율적이므로
for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
print(cnt)