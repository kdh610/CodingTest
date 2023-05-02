import sys

n,c = map(int,input().split())

house = [ int(sys.stdin.readline()) for _ in range(n)]


house.sort()

left =0
right = int(1e9)
answer=0
while left<=right:
    mid = (left+right)//2
    cnt=1
    temp= house[0]
    for i in range(1,len(house)):
        if house[i] - temp >= mid:
            cnt+=1
            temp=house[i]

    if cnt < c:
        right = mid-1
    else:
        answer=max(answer,mid)
        left = mid+1


print(answer)