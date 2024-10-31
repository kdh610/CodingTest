import sys
from collections import *

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

counter =Counter(arr)
answer=0
arr.sort()
for i in range(n-1,-1,-1):
    # print('i',arr[i])
    for j in range(n-1,-1,-1):
        if j==i:
            continue
        if counter[arr[i] - arr[j]]:
            answer+=1
            if arr[i]== 2*arr[j] and counter[arr[j]]<3:
                # print('두배')
                answer-=1
                continue
            if arr[j]==0 and counter[arr[i]]<2:
                answer-=1
                continue

            break
    # print(answer)

print(answer)