

n = int(input())

INF = 100000
dp=[INF]*(n+1)
check = True

if n==3 or n==1:
    check=False


if n>=5:
    dp[2]= 1
    dp[4] = 2
    dp[5] = 1
elif n==2:
    dp[2] = 1
elif n==4:
    dp[2] = 1
    dp[4] = 2

for i in range(6,n+1):
    dp[i] = min(dp[i-2] +1, dp[i-5]+1)

if check:
    print(dp[n])
else:
    print(-1)
