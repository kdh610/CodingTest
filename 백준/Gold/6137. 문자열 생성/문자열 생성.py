from collections import *


n = int(input())

S = deque()

for _ in range(n):
    S.append(input())

T = deque()
answer = ''.join([ 'Z' for _ in range(n)])



def compare(start,end):

    if S[start] < S[end]:
        T.append(S.popleft())

        return 0
    elif S[start] > S[end]:
        T.append(S.pop())

        return -1

    return 2

start = 0
end = n-1
while S:

    result = compare(start,end)

    if result==2:
        start+=1
        end-=1
    else:
        n-=1
        start=0
        end=n-1

    if start>=end:
        T.append(S.pop())
        n-=1
        start=0
        end=n-1

answer = ''.join(T)

for i in range(0,len(answer),80):
    
    print(answer[i:i+80])




