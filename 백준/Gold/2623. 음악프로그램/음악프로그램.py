

from collections import *

N,M = map(int,input().split())

inCount=[0] * (N+1)

graph = defaultdict(list)


for _ in range(M):
    order = list(map(int,input().split()))

    if len(order)>=3:
        for i in range(2,len(order)):
            graph[order[i-1]].append(order[i])
            inCount[order[i]]+=1




Q = deque()

for i in range(1,N+1):
    if inCount[i]==0:
        Q.append(i)
answer=[]
cnt=0
while Q:
    start = Q.popleft()
    if inCount[start]==0:
        answer.append(start)
        cnt+=1

    for i in graph[start]:
        inCount[i]-=1
        if inCount[i]==0:
            Q.append(i)

if cnt==N:
    print(*answer,sep='\n')
else:
    print(0)