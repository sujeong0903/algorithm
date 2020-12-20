# 동전 0

n, k = map(int, input().split())
array = []
cnt = 0
for _ in range(n):
    array.append(int(input()))
#동전이 큰 것 부터 처리한다. 
for i in range(len(array)-1, -1, -1):
    if array[i] > k: continue
    cnt += k//array[i]
    k %= array[i]
print(cnt)

