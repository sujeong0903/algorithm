#위장

def solution(clothes):
    answer = 1
    hash = dict()
    for x in clothes: hash[x[1]] = hash.get(x[1], 0) + 1
    for n in hash.values():
        answer *= (n + 1)
    return answer-1 # 모두 착용 안했을 때 빼주기

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))