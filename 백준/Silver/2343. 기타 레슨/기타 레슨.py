import sys

N,M = map(int,input().split())
lecture = list(map(int,sys.stdin.readline().split()))

start,end=max(lecture),int(1e9)
total=sum(lecture)
answer=int(1e9)
while start<=end:
    mid = (start+end)//2

    cnt=1
    sum=0
    for i in lecture:
        if sum+i<=mid:
            sum+=i
        else:
            cnt+=1
            sum=i

    if cnt>M:
        start=mid+1
    else:
        end = mid - 1
        answer=min(answer,mid)

print(answer)