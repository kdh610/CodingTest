import sys


n=int(input())
k=int(input())


start,end=1,int(1e10)
answer=0
while start<=end:

    mid=(start+end)//2

    cnt=0
    for i in range(1,n+1):
        if n*i<mid:
            cnt+=n
        else:
            cnt+=mid//i

    if cnt>=k:
        end=mid-1
        answer=mid
    else:
        start=mid+1


print(answer)