from collections import *
def solution(maps):
    visit = [[False]*len(maps[0]) for _ in range(len(maps))]

    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    Q = deque()
    result = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!='X' and not visit[i][j]:
                Q.append((i,j))
                visit[i][j]=True
                sum=int(maps[i][j])
                while Q:
                    y,x = Q.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0<=ny<len(maps) and 0<=nx<len(maps[0]) and not visit[ny][nx] and maps[ny][nx]!='X':
                            sum+=int(maps[ny][nx])
                            visit[ny][nx]=True
                            Q.append((ny,nx))

                result.append(sum)
    if not result:
        result.append(-1)

    result.sort()
                
                
    return result