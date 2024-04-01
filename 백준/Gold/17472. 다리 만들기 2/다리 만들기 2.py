from collections import *
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
dy=[0,0,1,-1]
dx=[1,-1,0,0]

island_num=1
Q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j]==1 and not visit[i][j]:
            island_num += 1
            Q.append((i,j))
            visit[i][j] = True
            board[i][j] = island_num
            while Q:
                y,x = Q.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0<=ny<N and 0<=nx<M and board[ny][nx]==1:
                        board[ny][nx] = island_num
                        Q.append((ny,nx))
                        visit[ny][nx] = True
#print(*board,sep='\n')

graph = []

for i in range(N):
    for j in range(M):
        if board[i][j]!=0:
            start = board[i][j]
            end = -1
            Q.append((i,j))

            while Q:
                y,x = Q.popleft()
                #print('y,x',y,x)
                for k in range(4):
                    length = 0
                    ny = y + dy[k]
                    nx = x + dx[k]

                    while 0<=ny<N and 0<=nx<M and board[ny][nx]==0:
                        #print('ny,nx', ny, nx, board[ny][nx])
                        length+=1
                        ny+=dy[k]
                        nx+=dx[k]

                        if ny<0 or ny>=N or nx<0 or nx>=M: break

                        if board[ny][nx]!=0 and length>=2:
                            #print(ny,nx, board[ny][nx])
                            end=board[ny][nx]
                            graph.append((start,end,length))
                            #print(graph)
                            break

#print(graph)


parent = [ i for i in range(island_num+1)]


def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a==b: return False

    parent[b] = a
    return True

graph.sort(key=lambda x:x[2])

sum=0
cnt=1
for i in graph:
    a,b,c = i

    if not union(a,b): continue
    sum+=c
    cnt+=1
    if cnt==island_num-1:
        break

if cnt!=island_num-1:
    print(-1)
else:
    print(sum)