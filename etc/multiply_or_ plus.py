# 곱하기 혹은 더하기

#각 자리가 숫자로 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' or '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 
array = input()
sum = int(array[0])
for i in range(1, len(array)):
    # 두 수 중에 하나라도 '0' or '1'인 경우, 곱하기 보다는 더하기 수행
    num = int(array[i])
    if sum <= 1 or num <=1:
        sum+=num
    else:
        sum*=num
print(sum)

#더하기 보단 곱하기가 값을 크게 만든다. 0일때를 제외하곤 *를 수행하는게 효율 적