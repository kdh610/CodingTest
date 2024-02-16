


N = int(input())

rgb =[ list(map(int,input().split())) for _ in range(N)]

answer = int(1e9)
for i in range(3):
    #print('i======',i)
    dp=[[0,0,0] for _ in range(N)]
    dp[0][i] = rgb[0][i]

    for j in range(1,N):

        for k in range(3):
            if dp[j-1][(k+1)%3]==0 and dp[j-1][(k+2)%3]==0:
                dp[j][k]=0
            elif dp[j-1][(k+1)%3]!=0 and dp[j-1][(k+2)%3]!=0:
                dp[j][k] = min(dp[j-1][(k+1)%3],dp[j-1][(k+2)%3]) + rgb[j][k]
            else:
                dp[j][k] =rgb[j][k]+dp[j-1][(k+1)%3] if dp[j-1][(k+1)%3]!=0 else dp[j-1][(k+2)%3]+rgb[j][k]




    #print(*dp,sep="\n")
    min_value = min(dp[N-1][(i+1)%3], dp[N-1][(i+2)%3])

    answer=min(answer,min_value)

print(answer)
