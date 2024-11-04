import sys


n = int(input())
liquid = list(map(int,sys.stdin.readline().split()))

left, right = 0, n-1
result = abs(liquid[left] + liquid[right])
answer = [liquid[left], liquid[right]]

while left < right:
    temp = liquid[left] + liquid[right]
    # print('l, r',left,right)
    # print('temp',temp)

    if abs(temp) < result:
        result = abs(temp)
        answer = [liquid[left], liquid[right]]


    if temp<0:
        left+=1
    else:

        right-=1


print(*answer)





