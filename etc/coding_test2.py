# 문자 압축 해제 문제
#10(p) = pppppppppp 3(hi) = hihihi 2(2(hi)co) = hihicohihico 
# 2(2(hi)2(co))x2(bo) = hihicocohihicocoxbobo


strs = "2(2(hi)2(co))xs2(bo)sdf"
answer = ""
stack = []
value = ""
is_num = True


for ch in strs:
    if ch == "(":
        stack.append(value)
        value = ""
    elif ch==")":
        n = 1
        while True:
            if stack[-1].isnumeric() == True:
                n = int(stack.pop())
                break
            else:
                value = stack.pop() + value
        stack.append(value * n)
        value = ""
    else:
        if len(value) == 0:
            is_num = ch.isnumeric()
            value = ch
        elif is_num == ch.isnumeric():
            value += ch
        else:
            stack.append(value)
            value = ch
            is_num = ch.isnumeric()

#  누락된 부분
if value != "":
    stack.append(value)
    
while stack:
    answer += stack.pop(0)

print(answer)
