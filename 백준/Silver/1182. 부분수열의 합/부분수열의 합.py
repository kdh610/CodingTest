import sys
from itertools import *

n,s = map(int,input().split())

numbers = list(map(int,sys.stdin.readline().split()))

answer=0

for i in range(1,n+1):

    comb = list(combinations(numbers,i))

    for j in comb:

        if sum(j)==s:
            answer+=1

print(answer)

