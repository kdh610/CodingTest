
n, k = map(int,input().split())



xy = [(0,0)]

for _ in range(n):
    x,y = map(int,input().split())
    xy.append((x,y))


distance= [ [0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        distance[i][j] = abs(xy[i][0] - xy[j][0]) + abs(xy[i][1] - xy[j][1])


dp = [[int(1e9)]*(k+1) for _ in range(n+1) ]

dp[1][0] = 0

for i in range(2,n+1):
    #print('i=============',i)
    for j in range(k+1):
        #print('j=======',j)
        for a in range(j+1):
            # print('a===',a)
            # print('[',i-a-1,']',j-a)
            dp[i][j] = min(dp[i][j], dp[i-a-1][j-a] + distance[i-a-1][i])


#print(*dp, sep='\n')

print(min(dp[n]))
