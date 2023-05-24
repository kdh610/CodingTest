from collections import *
import sys
T = int(input())

dy = [0,0,1,-1]
dx = [1,-1,0,0]

for _ in range(T):
    # 입력값 초기화
    w, h = map(int,sys.stdin.readline().split())
    building=[ list(sys.stdin.readline().strip()) for _ in range(h)]

    answer = []
    fire=[]
    Q = deque()

    for i in range(h):
        for j in range(w):
            if building[i][j]=='*':
                Q.append((i,j))
            elif building[i][j]=='@':
                cur = (i,j)
                building[i][j]=0

    Q.appendleft(cur)

    while Q:
        y,x = Q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<h and 0<=nx<w:
                # 사람일때
                if isinstance(building[y][x], int) and building[ny][nx] == '.':
                    building[ny][nx] = building[y][x] + 1
                    Q.append((ny, nx))
                # 불일때
                elif building[y][x]=='*' and building[ny][nx]!='#' and  building[ny][nx]!='*':
                    building[ny][nx] = '*'
                    Q.append((ny,nx))
            else:
                if isinstance(building[y][x], int):
                    answer.append(building[y][x] + 1)
                    break



    if len(answer)==0:
        print('IMPOSSIBLE')
    else:
        print(min(answer))









