

from collections import *



N,M = map(int,input().split())

maze = [ list(input()) for _ in range(N)]

visit = [[ [0]*M for _ in range(N)] for _ in range(64)]


Q= deque()

for i in range(N):
    for j in range(M):
        if maze[i][j]=='0':
            Q.append((i,j,0))
            visit[0][i][j] =1

dy = [0,0,1,-1]
dx = [1,-1,0,0]
key_list = ['a','b','c','d','e','f']
door_list = ['A','B','C','D','E','F']

answer=-1

move = 0
while Q:
    move+=1
    size = len(Q)
    flag = False
    #for i in range(size):
    y, x, cur_key = Q.popleft()


    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        nkey = cur_key

        if 0<= ny <N and 0<=nx<M:
            if maze[ny][nx]=='#' or visit[cur_key][ny][nx]!=0: continue


            if maze[ny][nx] in key_list:
                shift = ord(maze[ny][nx]) - ord('a')
                gotkey = 1<<shift
                nkey = nkey | gotkey
                #maze[ny][nx]='.'

            elif maze[ny][nx] in door_list:
                shift = ord(maze[ny][nx]) -ord('A')
                door = 1<<shift
                if cur_key & door ==0: continue

            visit[nkey][ny][nx] = visit[cur_key][y][x]+1

            if maze[ny][nx] == '1':
                answer = visit[cur_key][y][x]
                flag=True
                break


            Q.append((ny,nx,nkey))

    if flag: break

print(answer)




