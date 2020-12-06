#완주하지 못한 선수

def solution(participant, completion):
    d = {} #dictionary 선언

    for x in participant: d[x] = d.get(x,0)+1
    for x in completion: d[x] -= 1
    for x in d:
        if(d[x] != 0):
            return x