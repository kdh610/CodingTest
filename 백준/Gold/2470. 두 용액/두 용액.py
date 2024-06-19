
# 10
# -87 -42 -40 -22 -11 23 29 78 79 98
#
# -22 23  #정답
# -22 29  #출력

import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

result = int(2e9) +1

start = 0
end = n-1

answer = [arr[start], arr[end]]



while start<end:
    hap = abs(arr[start] + arr[end])


    if hap < result:
        result = hap
        answer = [arr[start], arr[end]]


    if arr[start] + arr[end] <0:
        start+=1
    else:
        end-=1


print(answer[0], answer[1])