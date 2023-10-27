import sys

k,n = map(int,input().split())

lan = [int(sys.stdin.readline().strip()) for _ in range(k)]

start,end= 1,int(2e31)-1
answer=0
while start<=end:
    mid=(start+end)//2

    cnt=0
    for i in lan:
        cnt+=i//mid


    if cnt<n:
        end=mid-1
    else:
        start=mid+1
        answer=max(answer,mid)

print(answer)
