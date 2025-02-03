from collections import *
def solution(order):
    stack = deque()
    Q = deque()

    for i in range(len(order)):
        Q.append(i+1)


    idx = 0
    box = False
    sub = False

    while True:

        if Q and Q[0]==order[idx]:
            Q.popleft()
            idx+=1
        elif stack and stack[-1]==order[idx]:
            stack.pop()
            idx+=1
        elif Q and Q[0]!=order[idx]:
            stack.append(Q.popleft())
        else:
            break
    
    return idx