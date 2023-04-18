import sys

n,m = map(int,input().split())

arr=[int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

dif=-1
answer = int(2e9)+1
end = 0

for i in range(n):
    if end==n:
        end-=1
    if end<n:
        dif = arr[end] - arr[i]
    while dif<m and end<n:
        dif = arr[end] - arr[i]
        end+=1


    if dif>=m:
        answer = min(answer,dif)





print(answer)

