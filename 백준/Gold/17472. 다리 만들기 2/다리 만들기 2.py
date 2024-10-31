
from collections import *

n,m = map(int, input().split())

island = [ list(map(int,input().split())) for _ in range(n)]

island_dict = defaultdict(list)
number = 2
visit = [ [False]*m for _ in range(n)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(y,x, number):
    q = deque()
    q.append((y,x))
    visit[y][x] = True
    island[y][x] = number
    island_dict[number].append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and not visit[ny][nx]:
                if island[ny][nx]==1:
                    visit[ny][nx] = True
                    island[ny][nx] = number
                    island_dict[number].append((ny, nx))
                    q.append((ny,nx))


for i in range(n):
    for j in range(m):
        if island[i][j]==1:
            bfs(i,j,number)
            number+=1


bridge = set()


for i in island_dict:
    for y,x in island_dict[i]:

        for j in range(4):
            ny = y+dy[j]
            nx = x+dx[j]

            if 0<=ny<n and 0<=nx<m and island[ny][nx]==0:
                length = 1
                while True:
                    ny += dy[j]
                    nx += dx[j]

                    if 0<=ny<n and 0<=nx<m:
                        if island[ny][nx] == 0:
                            length+=1
                            continue
                        else:
                            if island[ny][nx]==island[y][x]:
                                break


                            if length>=2:
                                bridge.add((island[y][x], island[ny][nx], length))
                                break
                            else:
                                break
                    else:
                        break

parent = [ i for i in range(number+1)]

def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(a,b):
    a=find(parent,a)
    b=find(parent,b)

    if a==b:
        return False

    parent[b]=a
    return True

bridge = list(bridge)
bridge.sort(key=lambda x:x[2])

# print(*island, sep='\n')
# print(island_dict)
#
# print(bridge)

cost=0
cnt=0
# print(number)
for b in bridge:
    a,b,c = b

    if not union(a,b):
        continue

    cnt+=1
    cost+=c
    if cnt==number-3:
        print(cost)
        break
else:
    print(-1)


