
from itertools import *
N = int(input())

synergy = [list(map(int,input().split())) for _ in range(N)]
arr = [i for i in range(N)]

# print(synergy)
# 
# print(list(combinations(arr,int(N/2))))
answer = int(1e9)

for i in list(combinations(arr,int(N/2))):
    #print('i',i)
    startTeam = list(i)
    linkTeam = []

    for j in range(N):
        if j not in startTeam:
            linkTeam.append(j)

    sumStart =0
    sumLink = 0
    for j in list(combinations(startTeam,2)):
        #print(j)
        sumStart+=synergy[j[0]][j[1]]
        sumStart += synergy[j[1]][j[0]]

    for j in list(combinations(linkTeam, 2)):
        #print(j)
        sumLink += synergy[j[0]][j[1]]
        sumLink += synergy[j[1]][j[0]]

    answer=min(answer,abs(sumStart-sumLink))

print(answer)