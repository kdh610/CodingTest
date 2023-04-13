import sys
n, c = map(int,input().split())
house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()
answer = 0
left, right = 1, house[-1]

while left<=right:
    mid = (left+right)//2
    cnt = 1
    cur = house[0]
    check=False
    for i in range(1,len(house)):
        dis = house[i] -cur
        if dis==mid:
            check=True
        if dis < mid:
            continue
        else:
            cnt+=1
            cur = house[i]
    if cnt < c:
        right = mid-1
    elif cnt>=c:
        left = mid+1
        answer = max(answer, mid)



print(answer)