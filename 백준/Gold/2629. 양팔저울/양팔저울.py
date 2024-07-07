

n = int(input())
weight = [0]+list(map(int,input().split()))

m = int(input())
marbles = list(map(int,input().split()))
sorted_marble = sorted(marbles)
max_weight = sum(weight)

dp = [ [True] + [False]*(40001) for _ in range(n+1) ]

for i in range(1,n+1):
    w = weight[i]
    #print('w',w)
    #print(dp[i-1])
    for j in range(max_weight):
        #print('j',j)
        if dp[i-1][j]:
            #print('구슬',j)
            dp[i][j] = True
            dp[i][abs(j-w)] = True
            dp[i][abs(j+w)] = True

            #print(dp[i])

answer = []
for marble in marbles:
    if dp[n][marble]:
        answer.append('Y')
    else:
        answer.append('N')
print(*answer)