


c, n =map(int,input().split())

cities = [[0,0]] + [ list(map(int,input().split())) for _ in range(n) ]

dp = [ [0]+[int(1e9)]*(1101) for _ in range(n+1)]
answer = int(1e9)
for i in range(1,n+1):
    cost = cities[i][0]
    cnt = cities[i][1]
    for j in range(1,1101):

        # if j%cnt==0:
        idx=1
        # print('=====j',j)
        # print('cost',cost)
        # print('cnt',cnt)
        while True:
            # print('idx',idx)
            # print(dp[i - 1])
            if j-(cnt*idx)<0:
                break
            if dp[i-1][j- (cnt*idx)] != int(1e9):
                dp[i][j] = min(dp[i-1][j],  dp[i-1][j-(cnt*idx)] + (cost*idx), dp[i][j] )
                #print(dp[i][j])
            idx+=1
        if dp[i][j]==int(1e9): dp[i][j] = dp[i-1][j]

        if i==n and j>=c:
            answer=min(answer, dp[i][j])


print(answer)