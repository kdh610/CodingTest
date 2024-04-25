dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = int(1e9)


def back_tracking(cost_arr,visit,board,N,y,x,dir,cost):
    global answer
    if cost_arr[y][x]<cost:
        
        return
    else:
        cost_arr[y][x] = cost

    if y==N-1 and x==N-1:
        answer = min(answer,cost)
        return
    if cost>answer:
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<N and board[ny][nx]==0 and not visit[ny][nx]:

            money=100
            if (0<=dir<=1 and i>=2) or (dir>=2 and 0<=i<=1):
                money=600
            if cost+money>cost_arr[ny][nx]: continue

            cost_arr[y][x]=cost+money
            visit[ny][nx] = True


            back_tracking(cost_arr,visit,board,N,ny, nx, i, cost+money)
            visit[ny][nx] = False


def solution(board):
    global answer
    N = len(board)

    visit=[[False]*N for _ in range(N)]
    visit[0][0]=True
    cost_arr = [[int(1e9)]*N for _ in range(N)]

    back_tracking(cost_arr,visit,board,N,0,0,-1,0)

    return answer