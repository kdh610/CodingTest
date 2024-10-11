


T = int(input())

for _ in range(T):
    n = int(input())
    coins = [0]+list(map(int,input().split()))
    price = int(input())

    dp = [ [1]+[0]*(price) for _ in range(n+1) ]

    for i in range(1,n+1):
        coin = coins[i]
        for j in range(1,price+1):
            if coin > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] += dp[i][j-coin] + dp[i-1][j]


    print(dp[n][price])


