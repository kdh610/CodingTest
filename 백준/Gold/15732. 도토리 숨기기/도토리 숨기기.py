import math
import sys


n,k,d = map(int,input().split())

rules = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]
start,end=1,n

while start<=end:

    mid=(start+end)//2

    acorn=0

    for a,b,c in rules:
        box = min(mid,b)
        if box>=a:
            acorn+=(box-a)//c +1


    if acorn>=d:
        end=mid-1
        answer=mid
    else:
        start=mid+1




print(answer)