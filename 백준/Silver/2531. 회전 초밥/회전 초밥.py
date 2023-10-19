from collections import *
import sys

N, d, k, c = map(int, input().split())
belt = [int(sys.stdin.readline().strip()) for _ in range(N)]

left, right = 0,0
sushi = defaultdict(int)

answer=0
temp=0

sushi[c]=1
while right<k:
    sushi[belt[right]]+=1
    right+=1


while left<N:
    answer = max(answer, len(sushi))

    sushi[belt[left]]-=1
    sushi[belt[right]]+=1

    if sushi[belt[left]]==0:
        del sushi[belt[left]]

    right=(right+1)%N
    left=(left+1)


print(answer)



