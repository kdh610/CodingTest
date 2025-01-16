from collections import *
answer = int(1e9)


def bfs(y, x, board, len_y, len_x, visit):
    global answer

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    Q = deque()
    Q.append((y,x))

    while Q:
        y,x = Q.popleft()

        if board[y][x] == 'G':
            answer = min(answer, visit[y][x])

        for i in range(4):
            ny = y
            nx = x
            while True:
                if not (0 <= ny + dy[i] < len_y) or not (0 <= nx + dx[i] < len_x) or board[ny + dy[i]][nx + dx[i]] == 'D':
                    break
                ny += dy[i]
                nx += dx[i]

            if board[ny][nx] == 'R':
                continue

            if visit[ny][nx] == 0 or visit[ny][nx] >= visit[y][x] + 1:
                visit[ny][nx] = visit[y][x] + 1
                Q.append((ny,nx))


def solution(board):
    global answer
    sy, sx = -1, -1
    len_y = len(board)
    len_x = len(board[0])
    visit = [[0] * len_x for _ in range(len_y)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                sy = i
                sx = j

    bfs(sy, sx, board, len_y, len_x, visit)

    if answer == int(1e9):
        answer = -1

    # print(answer)
    return answer