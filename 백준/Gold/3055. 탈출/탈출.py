from collections import *

R,C = map(int,input().split())

field = []
sx,sy=0,0
waters=[]
for i in range(R):
    field.append(list(input()))

for i in range(R):
    for j in range(C):
        if field[i][j]=='S':
            field[i][j] =0
            sy,sx=i,j
        if field[i][j]=='*':
            waters.append((i,j))
        if field[i][j]=='D':
            by,bx=i,j
dx=[0,0,1,-1]
dy=[1,-1,0,0]

Q = deque()

Q.append((sy,sx))
for w in waters:
    Q.append(w)

while Q:
    y,x = Q.popleft()
    if str(field[by][bx]).isdigit() or field[by][bx]=='*':
        break
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<R and 0<=nx<C:
            if str(field[y][x]).isdigit():
                if field[ny][nx]=='.' or field[ny][nx]=='D':
 
                    field[ny][nx]=field[y][x]+1
                    Q.append((ny,nx))

            if field[y][x]=='*':
                if field[ny][nx] == '.' or str(field[ny][nx]).isdigit():
                    field[ny][nx] = '*'
                    Q.append((ny, nx))


if field[by][bx]=='D':
    print("KAKTUS")
else:
    print(field[by][bx])







