

n,m = map(int,input().split())

app_meomory =[0]+ list(map(int,input().split()))
app_cost = [0]+ list(map(int,input().split()))

answer = sum(app_cost)
memory_dp = [[0]*(sum(app_cost)+1) for _ in range(n+1)]

for i in range(1,n+1):
    memory = app_meomory[i]
    cost = app_cost[i]
    #print(memory, cost)
    for j in range(sum(app_cost)+1):
        #print(j)
        if cost > j:
            memory_dp[i][j] = memory_dp[i-1][j]
        else:
            memory_dp[i][j] = max(memory_dp[i-1][j], memory_dp[i-1][j-cost] + memory)

        # if memory_dp[i][j] >= m:
        #     answer=min(answer,j)

    #print(*memory_dp,sep='\n')

for i, mem in enumerate(memory_dp[n]):
    if mem>=m:
        print(i)
        break