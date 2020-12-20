# ATM

n = int(input())
data = list(map(int, input().split()))
data.sort()
sum = 0
result = 0
for num in data:
    sum += num
    result += sum
print(result)