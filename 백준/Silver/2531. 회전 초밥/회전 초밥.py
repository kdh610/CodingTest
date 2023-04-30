from collections import *
import sys

# 접시수, 초밥종류, 연속해서 먹는 접시, 쿠폰번호
N, d, k, c = map(int,input().split())

belt = [ int(sys.stdin.readline().strip()) for _ in range(N)]

start,end=0,0
answer = 0
temp = deque()

while True:
    cnt = 0

    while len(temp)<k:
        temp.append(belt[end])
        end+=1


    if c not in temp:
        cnt=1

    cnt += len(set(temp))


    answer = max(answer,cnt)

    end= (end+1)%N
    start= (start+1)%N

    temp.popleft()
    temp.append(belt[end-1])

    if start==0 and end==k:
        break

print(answer)