




n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]



dp = [[[-1*2e9]*3 for _ in range(m)] for _ in range(n)]


for i in range(m):
    dp[0][i][1] = arr[0][i]


for i in range(1,m):
    dp[0][i][1] += dp[0][i-1][1]


for i in range(1,n):
    for j in range(m):
        dp[i][j][1] = max(dp[i - 1][j]) +  arr[i][j]
        dp[i][j][0] = max(dp[i][j-1][0], dp[i][j-1][1]) +  arr[i][j]

    for k in range(m-2,-1,-1):
        dp[i][k][2] = max(dp[i][k + 1][2], dp[i][k + 1][1]) +  arr[i][k]



print(max(dp[n-1][m-1]))