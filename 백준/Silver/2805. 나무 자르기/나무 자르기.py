
import sys

n,m = map(int,input().split())

trees = list(map(int,sys.stdin.readline().split()))

right = int(1e9)
left = 1
answer=0

while left<=right:
    length=0
    mid = (left+right)//2

    for tree in trees:
        if tree>mid:
            length+=tree-mid

        
    if length<m:
        right=mid-1
    else:
        answer = max(answer, mid)
        left=mid+1

print(answer)