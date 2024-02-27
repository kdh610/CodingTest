import sys
from collections import *

n = int(input())

rgb = []

for i in range(n):
    rgb.append(list(map(int,sys.stdin.readline().split())))

dp = [[0] * 3 for _ in range(n)]

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i - 1][1] + rgb[i][0], dp[i - 1][2] + rgb[i][0])
    dp[i][1] = min(dp[i - 1][0] + rgb[i][1], dp[i - 1][2] + rgb[i][1])
    dp[i][2] = min(dp[i - 1][0] + rgb[i][2], dp[i - 1][1] + rgb[i][2])

print(min(dp[n-1]))
