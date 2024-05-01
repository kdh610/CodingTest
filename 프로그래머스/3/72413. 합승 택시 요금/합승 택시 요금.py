from collections import *

def solution(n, s, a, b, fares):
    graph = defaultdict(list)

    for fare in fares:
        x,y,z = fare
        graph[x].append((y,z))
        graph[y].append((x,z))


    cost = [[int(1e9)]*(n+1) for _ in range(n+1)]

    for i in graph:
        for j in graph[i]:
            cost[i][j[0]]=j[1]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                cost[i][j] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])


    #print(*cost,sep='\n')

    answer = cost[s][a] + cost[s][b]


    for i in range(1,n+1):
        if cost[s][i]!=int(1e9):
            cost_ab = cost[s][i]
            cost_a = cost[i][a]
            cost_b= cost[i][b]
            # print('i',i)
            # print('ab',cost_ab)
            # print('a',cost_a)
            # print('b',cost_b)
            # print('ans',cost_ab+ cost_a + cost_b)
            answer = min(answer, cost_ab+ cost_a + cost_b)
    return answer