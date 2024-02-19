import sys

n = int(input())

wines = [int(sys.stdin.readline().strip()) for _ in range(n)]


dp = [0] *n
dp[0] = wines[0]

if n>1:
    dp[1] = wines[0]+wines[1]
if n>2:
    dp[2] = max(wines[2]+wines[1], wines[2]+wines[0], dp[1])

if n>3:
    for i in range(3,n):
        dp[i] = max(dp[i-1], wines[i]+wines[i-1]+dp[i-3], wines[i]+dp[i-2])



print(dp[n-1])