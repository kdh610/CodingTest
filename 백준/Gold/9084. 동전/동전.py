
T = int(input())

for _ in range(T):

    n = int(input())
    value = list(map(int,input().split()))
    m = int(input())

    dp= [0]*(m+1)
    dp[0] = 1

    for v in value:

        for j in range(1,m+1):
            if j>= v:
                dp[j] += dp[j-v]
    print(dp[m])





