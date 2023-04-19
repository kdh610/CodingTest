import sys

n = int(input())
budget = list(map(int,sys.stdin.readline().split()))
limit = int(input())

if sum(budget)<=limit:
    print(max(budget))
    exit(0)


left = 1
right = int(1e9)
answer=0

while left<=right:
    mid = (left+right)//2
    total = 0

    for i in budget:
        if i<mid:
            total+=i
        else:
            total+=mid

    if total>limit:
        right=mid-1
    else:
        answer=max(answer,mid)
        left=mid+1

print(answer)
