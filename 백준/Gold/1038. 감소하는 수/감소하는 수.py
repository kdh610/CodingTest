
from collections import *

N = int(input())


Q = deque()
num = 1
cnt = 0
answer=-1

for i in range(1,10):
    Q.append(i)

if 0<=N<10:
    answer=N

else:
    while Q:

        num = Q.popleft()
        cnt+=1
        #print('num',num, cnt)
        if cnt==N:
            answer = num
            break

        for i in range(num%10):
            Q.append(num*10 + i)



print(answer)