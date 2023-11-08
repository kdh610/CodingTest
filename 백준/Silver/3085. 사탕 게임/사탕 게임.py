import sys
import copy


n=int(input())

candies=[list(sys.stdin.readline().strip()) for _ in range(n)]

dy=[0,0,1,-1]
dx=[1,-1,0,0]

global answer
answer=0


def swap(y,x, ny,nx):
    temp = candies
    temp[y][x], temp[ny][nx] = temp[ny][nx], temp[y][x]

    count(temp,y,x)
    count(temp,ny,nx)
    temp[ny][nx], temp[y][x] = temp[y][x], temp[ny][nx]

def count(temp,y,x):

    global answer
    r_cnt=0
    r_tmp = temp[y][0]
    c_cnt = 0
    c_tmp = temp[0][x]
    for i in range(n):

        if temp[y][i] == r_tmp:
            r_cnt+=1

        else:
            r_tmp = temp[y][i]
            r_cnt=1
        if temp[i][x] == c_tmp:
            c_cnt += 1
        else:
            c_tmp = temp[i][x]
            c_cnt = 1

        answer=max(answer,r_cnt,c_cnt)

    

for i in range(n):
    for j in range(n):

        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]

            if 0<=ny<n and 0<=nx<n:
                swap(i,j,ny,nx)

print(answer)