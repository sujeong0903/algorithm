# 소수 찾기
# 제한사항
# - numbers는 길이 1 이상 7 이하인 문자열입니다.
# - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# - 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다

# 내 풀이 - 5, 8번 시간 초과...
# def isPrimeNumber(num):
#     if num <2: return False
#     for i in range(2, int(num**0.5)+1):
#         if num%i == 0:
#             return False
#     return True


# def solution(numbers):
#     answer = 0
#     nums = list(str(numbers))
#     nums.sort(reverse=True)
#     max_nums = int(''.join(nums))

#     for i in range(int(nums[len(nums)-1]), max_nums+1):
#         if i % 2 == 0 continue
#         if isPrimeNumber(i): 
#             datas = nums.copy()     # 얕은 복사!! 중요
#             for idx in range(len(str(i))):
#                 if str(i)[idx] in datas: datas.remove(str(i)[idx])
#                 else: break
#             else: answer += 1 # i의 값 이 모두 포함되었을 때
#     return answer

# print(solution(110))


# 남의 코드
from itertools import permutations

def isPrimeNumber(num):
    if num <2: return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        datas = permutations(numbers,i) # 조합 사용하기
        for number in datas:
            number = "".join(number)
            if isPrimeNumber(int(number)): 
                answer.add(int(number)) # 동일한 수 제거하기
                
    return len(answer)
print(solution("011"))