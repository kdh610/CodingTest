



n = int(input())

hp =[0]+ list(map(int,input().split()))
joy =[0] +list(map(int,input().split()))

answer = 0

dp = [ [0]*(101) for _ in range(n+1)]

for i in range(1,n+1):
    h = hp[i]
    j = joy[i]

    for k in range(101):

        if h >= k:
            dp[i][k] = dp[i-1][k]
        else:
            dp[i][k] = max(j + dp[i-1][k-h], dp[i-1][k])

print(dp[n][100])