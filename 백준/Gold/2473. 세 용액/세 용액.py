import sys


n = int(input())

liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

left, right = 0, n-1
result = max(abs(liquid[left]), abs(liquid[right])) * 3
answer = [liquid[left], liquid[right]]


for i in range(len(liquid)):
    left = i+1
    right = n-1
    while left<right:
        temp = liquid[i] + liquid[left] + liquid[right]
        if abs(temp) < result:
            result = abs(temp)
            answer = [liquid[i],liquid[left], liquid[right]]

        if temp<0:
            left+=1
        else:
            right-=1

answer.sort()
print(*answer)