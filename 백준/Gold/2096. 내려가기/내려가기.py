import sys

n = int(input())


max_tmp = [0]*3
min_tmp = [0]*3
MAX = [0]*3
MIN = [0]*3



for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    for j in range(3):
        if j==0:
            MAX[j] = a +  max(max_tmp[j], max_tmp[j+1])
            MIN[j] = a + min(min_tmp[j], min_tmp[j + 1])
        elif j==1:
            MAX[j] = b + max(max_tmp[j],  max_tmp[j+1],  max_tmp[j-1])
            MIN[j] = b + min(min_tmp[j], min_tmp[j + 1], min_tmp[j - 1])
        else:
            MAX[j] = c + max(max_tmp[j],  max_tmp[j-1])
            MIN[j] = c + min(min_tmp[j], min_tmp[j - 1])

    for i in range(3):
        max_tmp[i] = MAX[i]
        min_tmp[i] = MIN[i]

print(max(MAX),min(MIN))