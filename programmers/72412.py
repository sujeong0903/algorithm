# 순위 검색

# 내 풀이 1.
# 시간초과
# def solution(info, query):
#     answer = [0]*len(query)
    
#     for index, q in enumerate(query):
#         query_item = q.split(" and ")
#         lang = query_item[0]
#         job = query_item[1]
#         career = query_item[2]
#         food = query_item[3].split(" ")[0] 
#         score =  int(query_item[3].split(" ")[1])
#         for i in info:
#             user = i.split(" ")            
#             if lang != "-" and lang != user[0]:continue
#             if job != "-" and job != user[1]: continue
#             if career != "-" and career != user[2]: continue
#             if food != "-" and food != user[3]: continue
#             if int(user[4])>= score: answer[index] += 1               
#     return answer

#남의 풀이 2. 테이블
import bisect

lang = ["java", "python", "cpp"]
work = ["backend", "frontend"]
career = ["junior", "senior"]
food = ["pizza", "chicken"]

# - 일 경우 가능한 경우 모두 반복하기
def calc(table, a, b, c, d, e):
    rst = 0
    if a =='-':
        for item in lang:
            rst += calc(table, item, b,c,d,e)
    elif b == '-':
        for item in work:
            rst += calc(table, a, item ,c,d,e)
    elif c == '-':
        for item in career:
            rst += calc(table, a, b ,item,d,e)
    elif d == '-':
        for item in food:
            rst += calc(table, a, b ,c,item,e)
    else:
        index = bisect.bisect_left(table[a][b][c][d],e)
        rst = len(table[a][b][c][d]) - index 
    return rst

def solution(info, query):
    answer = []
    
    table = {}
    for a in lang:
        table[a] = {}
        for b in work:
            table[a][b]={}
            for c in career:
                table[a][b][c] = {}
                for d in food:
                    table[a][b][c][d] = []
    # 경우의 수 별로 리스트에 넣기
    for s in info:
        a,b,c,d,e= s.split(" ")
        table[a][b][c][d].append(int(e))
     
    # 리스트 정렬하기
    for a in lang:
        for b in work:
            for c in career:
                for d in food:
                    table[a][b][c][d].sort()
    for q in query: 
        a, aa, b, bb, c, cc, d, e = q.split(" ")
        answer.append(calc(table, a,b,c,d,int(e)))
        
    return answer