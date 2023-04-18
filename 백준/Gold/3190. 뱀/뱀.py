from collections import *

n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())

for i in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = -1
board[0][0] = 0

l = int(input())

move = defaultdict()
for i in range(l):
    sec, dir = input().split()
    move[sec] =dir


dy = [0,0,1,-1]
dx = [1,-1,0,0]
Q= deque()
sec = 0
dir = "right"
Q.append((0, 0))
while True:
    x,y = Q.pop()
    Q.append((x,y))
    

    if str(sec) in move:
        
        if dir=="right":
            if move[str(sec)]=='L':
                ny = y+dy[1]
                nx = x+dx[1]
                dir = "up"
            else:
                ny = y+dy[0]
                nx = x+dx[0]
                dir = "down"
        elif dir=="left":
            if move[str(sec)]=='L':
                ny = y+dy[0]
                nx = x+dx[0]
                dir = "down"
            else:
                ny = y+dy[1]
                nx = x+dx[1]
                dir = "up"
        elif dir=="up":
                if move[str(sec)] == 'L':
                    ny = y+dy[3]
                    nx = x+dx[3]
                    dir = "left"
                else:
                    ny = y+dy[2]
                    nx = x+dx[2]
                    dir = "right"
        else:
            if move[str(sec)] == 'L':
                ny = y+dy[2]
                nx = x+dx[2]
                dir = "right"
            else:
                ny = y+dy[3]
                nx = x+dx[3]
                dir = "left"

        if 0<=ny<n and 0<=nx<n and (nx,ny) not in Q:
            if board[nx][ny] == -1:
                board[nx][ny] = sec+1
                Q.append((nx,ny))
            else:
                board[nx][ny] = sec+1
                Q.append((nx, ny))
                Q.popleft()
        else:
            break

    else:    
        if dir == "right": 
            ny = y + dy[2]
            nx = x + dx[2]    
        elif dir == "left":   
            ny = y + dy[3]
            nx = x + dx[3]    
        elif dir == "up":   
            ny = y + dy[1]
            nx = x + dx[1]   
        else:
            ny = y + dy[0]
            nx = x + dx[0]
        if 0 <= ny < n and 0 <= nx < n and (nx, ny) not in Q:
            if board[nx][ny] == -1:
                board[nx][ny] = sec+1
                Q.append((nx, ny))
            else:
                board[nx][ny] = sec+1
                Q.append((nx, ny))
                Q.popleft()
        else:
            break
    sec+=1

print(sec+1)