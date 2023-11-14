import sys
n = int(input())
card = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1)
dp[1] = card[1]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(card[j] + dp[i-j], dp[i])

print(dp[n])

