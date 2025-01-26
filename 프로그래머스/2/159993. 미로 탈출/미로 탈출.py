import copy
from collections import *

def solution(maps):
    start=(-1,-1)
    lever = (-1,-1)
    end = (-1,-1)
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                start = (i,j)
            elif maps[i][j]=="L":
                lever = (i,j)
            elif maps[i][j]=="E":
                end = (i,j)
            elif maps[i][j]=='X':
                visit[i][j]='X'




    def bfs(y,x, visit, ey, ex):

        dy = [0,0,-1,1]
        dx = [1,-1,0,0]
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        new_map = copy.deepcopy(visit)

        Q = deque()
        Q.append((y,x))
        visited[y][x] = True

        while Q:
            y,x=Q.popleft()
            if y==ey and x==ex:
                return new_map[y][x]

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0<=ny<len(maps) and 0<=nx<len(maps[0]) and not visited[ny][nx]:
                    if new_map[ny][nx]=='X':
                        continue

                    new_map[ny][nx] = new_map[y][x]+1
                    visited[ny][nx]=True
                    Q.append((ny,nx))
        return 0

    answer=0
    toLever=0
    toEnd=0
    toLever=bfs(start[0],start[1],visit,lever[0],lever[1])

    if toLever!=0:
        toEnd=bfs(lever[0],lever[1],visit,end[0],end[1])
        answer=toLever+toEnd


    if answer==0 or answer==toLever:
        answer=-1

    answer=toLever+toEnd

    if answer==0 or answer==toLever:
        answer=-1
    return answer