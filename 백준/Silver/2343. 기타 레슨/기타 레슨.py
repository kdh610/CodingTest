import sys

n,m = map(int,input().split())

lecture = list(map(int,sys.stdin.readline().split()))

left = 1
right = int(1e9)
answer = int(1e9)

while left <= right:
    mid = (left+right)//2
    cnt = 1
    sum=0
    if mid<max(lecture):
        left =mid+1
        continue


    for i in lecture:
        sum+=i
        if sum>mid:
            sum=i
            cnt+=1



    if cnt>m:
        left=mid+1
    else:
        right = mid - 1
        answer=min(answer,mid)


print(answer)