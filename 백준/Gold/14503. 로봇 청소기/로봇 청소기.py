
n,m = map(int,input().split())
y,x,d = map(int,input().split())

field = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

cnt = 0


while True:
    if field[y][x]==0:
        cnt+=1
        field[y][x]=2

    temp = d
    check=False
    # 주변 쓰레기 확인
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m and field[ny][nx] == 0:
            check=True

    if check:
        d -= 1
        if d == -1:
            d = 3
        ny,nx= y+dy[d], x+dx[d]
        if 0 <= ny < n and 0 <= nx < m and field[ny][nx] == 0:
            y,x = ny,nx

    else:
        d= temp
        if d<=1:
            back= d+2
        else:
            back= d - 2
        ny = y + dy[back]
        nx = x + dx[back]
        if 0 <= ny < n and 0 <= nx < m and field[ny][nx] != 1:
            y, x = ny, nx
        else:
            break



print(cnt)





