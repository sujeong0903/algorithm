# 신규 아이디 추천

def solution(new_id):
    #1단계
    new_id = new_id.lower()
    answer = ''
    #2단계
    for ch in new_id:
        if ch.isalnum() or ch in '-_.':
            answer += ch
    #3단계 
    while '..' in answer:
        answer = answer.replace('..','.')
    #4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    #5단계
    answer = 'a' if answer == '' else answer 
    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer[:-1] if answer[-1] == '.' else answer
    #7단계
    while len(answer) <= 2:
        answer += answer[-1]    
    return answer

print(solution("abcdefghijklmn.p"))