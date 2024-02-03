from collections import * 
def solution(dartResult):
    stack = deque()
    for i in dartResult:

        if i.isdigit():
            if len(stack)>0 and stack[-1]==1 and i=='0':
                stack.pop()
                stack.append(10)
            else:
                stack.append(int(i))


        elif i=='*' or i=='#':
            if i=='*':
                stack[-1]*=2
                if len(stack)>1:
                    stack[-2]*=2
            else:
                stack[-1]*=-1
        else:
            num = stack.pop()
            square=0
            if i=='S':
                square=1
            elif i=='D':
                square=2
            else:
                square=3
            num = num**square
            stack.append(num)
        
    answer = 0
    for i in stack:
        answer+=i
    
    return answer