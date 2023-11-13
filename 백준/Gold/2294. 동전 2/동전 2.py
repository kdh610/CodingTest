import sys

n,k = map(int,sys.stdin.readline().split())

value = [int(sys.stdin.readline()) for _ in range(n)]
value.sort()

dp=[int(1e9)]*(k+1)
dp[0]=0
for i in range(1,k+1):

    for v in value:

        if v <= i:
            dp[i] = min(dp[i],dp[i-v]+1)


if dp[k]==int(1e9):
    print(-1)
else:
    print(dp[k])