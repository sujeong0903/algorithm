#1이 될 때까지
# n - 1
# n / k


# 가능한 많이 k로 나누기
# k로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있기 때문에
n, k = map(int, input().split())
cnt = 0

#1번 풀이 = n을 k로 나눌 수있으면 나누고, 나눌수 없으면 -1을 한다.
# while n > 1:
#     if n%k == 0:
#         n //= k
#     else:
#         n -= 1
#     cnt +=1
# print(cnt)
    

#2번째 풀이 - 입력값이 클 경우를 대비해서
while True:
    #N이 K로 나누어 떨어지는 수가 될때까지 빼기
    target = (n//k) * k
    cnt += (n - target) #1을 빼야하는 횟수
    n = target
    #N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    n //= k
    cnt += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
cnt += (n-1)
print(cnt)
