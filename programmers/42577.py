#전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if(phone_book[j].startswith(phone_book[i])): 
                # str.startswith(word) str이 word로 시작하는지 확인
                return False
    else:
        return True