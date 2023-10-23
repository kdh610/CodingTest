import sys

N,M = map(int,input().split())

trees = list(map(int,sys.stdin.readline().split()))

start = 0
end = int(1e9)

while start<=end:
    temp = 0
    height = (start+end)//2

    for t in trees:
        if t > height:
            temp+=t-height

    if temp<M:
        end = height-1
    elif temp>=M:
        start = height+1


print(end)
