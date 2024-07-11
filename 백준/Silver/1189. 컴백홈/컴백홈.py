



r, c,k = map(int,input().split())

arr = [ list(input()) for _ in range(r)]

arr[r-1][0]=1

dy = [0,0,1,-1]
dx = [1,-1,0,0]


visit = [[False]*c for _ in range(r)]
cnt = 1
answer = 0
def dfs(y, x, cnt):
    global answer
    # print("========== y,x",y,x)
    # print('cnt',cnt)
    if cnt==k and y==0 and x==c-1:
        answer+=1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<r and 0<=nx<c and not visit[ny][nx]:
            if arr[ny][nx]=='.':
                #print('ny,nx',ny,nx)
                visit[ny][nx]= True
                dfs(ny,nx, cnt+1)
                visit[ny][nx]=False



dfs(r-1,0 ,1)

print(answer)