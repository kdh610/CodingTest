import sys
import math

n=int(input())

dp=[int(1e9)]*(n+1)
dp[0]=0
square = [i*i for i in range(1,int(math.sqrt(n))+1) if i*i<=n]


for i in range(1,n+1):
    for v in square:
        if i>=v:
            if dp[i]>dp[i-v]+1:
                dp[i]=dp[i-v]+1




print(dp[n])


