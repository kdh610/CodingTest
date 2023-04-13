
import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))

dp=[0]*n

dp[0]=arr[0]

for i in range(1,n):
    dp[i] = max(dp[i-1]+arr[i], arr[i], arr[i]+arr[i-1])

print(max(dp))