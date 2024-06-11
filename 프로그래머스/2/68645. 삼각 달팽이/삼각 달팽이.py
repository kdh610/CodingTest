from collections import *
def solution(n):
    floor_cnt = defaultdict(int)
    snail = [[0] * n for _ in range(n)]
    num =1
    y, x = 0,0
    top = 0
    bottom = n-1
    dir= 0
    last = (n*(2 + (n-1))) /2

    while True:

        snail[y][x] = num
        num+=1
        floor_cnt[y]+=1

        if num == last+1: break

        if y==top and floor_cnt[y]==y+1:
            dir = 1
            top+=1
        elif y==bottom and floor_cnt[y] == y+1:
            dir = -1
            bottom-=1

        if y==bottom and x+1<n and dir==1:
            x+=1
        elif dir==1:
            y+= 1
        elif dir==-1:
            x-=1
            y-=1

    answer = []
    for i in range(n):
        for j in range(n):
            if snail[i][j]!=0:
                answer.append(snail[i][j])
    return answer