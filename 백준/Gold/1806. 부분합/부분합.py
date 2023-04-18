import sys

n,s = map(int,input().split())
arr = list(map(int,sys.stdin.readline().split()))

sum=0
answer=int(1e9)+1
start,end = 0,0

for i in range(n):
    while sum<s and end<n:
        sum += arr[end]

        end+=1

    if sum>=s:
        answer=min(answer,end-i)

    sum-=arr[i]

if answer==int(1e9)+1:
    print(0)
else:
    print(answer)




