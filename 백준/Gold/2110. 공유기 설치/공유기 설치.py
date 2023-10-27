import sys

n,c = map(int,input().split())
houses=[int(sys.stdin.readline().strip()) for _ in range(n)]

start, end = 1,int(1e9)
houses.sort()
answer=0

while start<=end:
    mid=(start+end)//2

    cnt=1
    now = houses[0]

    for house in houses[1:]:
        if house>=now+mid:
            cnt+=1
            now=house


    if cnt>=c:
        start=mid+1
        answer = max(answer, mid)
    elif cnt<c:
        end=mid-1



print(answer)


