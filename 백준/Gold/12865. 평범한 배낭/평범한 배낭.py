N,K = map(int,input().split())

stuffs = [list(map(int,input().split())) for _ in range(N)]
stuffs.insert(0,[0,0])

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    #print('i=====',i)
    w = stuffs[i][0]
    v = stuffs[i][1]
    for k in range(1,K+1):
        #print(k)
        if k<w:
            dp[i][k] = dp[i-1][k]

        else:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-w] + v)


print(dp[N][K])