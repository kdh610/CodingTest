from itertools import *
from collections import *
N = int(input())
height = list(map(int,input().split()))
index = [i for i in range(len(height))]

comb = list(combinations(index,2))
dict = defaultdict(int)

for i in range(len(comb)):
    legth = abs(height[comb[i][0]] + height[comb[i][1]])
    comb[i] = (legth,comb[i][0],comb[i][1])

comb.sort()
answer = int(1e9)
for i in range(len(comb)-1):
    elsa = comb[i]
    ana = comb[i+1]
    if elsa[1]==ana[1] or elsa[1]==ana[2] or elsa[2]==ana[1] or elsa[2]==ana[2]: continue
    answer = min(answer,abs(elsa[0]-ana[0]))

print(answer)