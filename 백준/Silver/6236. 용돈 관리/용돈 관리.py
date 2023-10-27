import sys

N,M = map(int,input().split())
expense = [ int(sys.stdin.readline().strip()) for _ in range(N)]

start, end = max(expense),int(1e9)
answer=int(1e9)
while start<=end:

    mid=(start+end)//2

    money = 0
    cnt = 1
    for i in expense:

        if money+i<=mid:
            money+=i
        else:
            money = i
            cnt+=1

    if cnt>M:
        start=mid+1
    else:
        end=mid-1
        answer=min(answer,mid)
print(answer)




