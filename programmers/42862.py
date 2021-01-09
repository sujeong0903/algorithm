# 체육복
#문제를 꼼꼼하게 읽자 
# n번 학생은 n-1 or n+1 학생에게만 체육복을 빌려줄 수 있다.
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost:
            answer += 1
        elif i in reserve:
            lost.remove(i)
            reserve.remove(i)
            answer+=1
    # 반복문을 돌릴때 remove하면 누락되는 요소가 생김. 

    # n-1, n+1 비교하기
    for i in lost:
        if i -1 in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
    return answer
    
print(solution(5, [4, 5], [1, 2, 3]))