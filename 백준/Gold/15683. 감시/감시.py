from itertools import *
from collections import *
import copy
n,m = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]

dir  = [(1,0),(0,1),(-1,0),(0,-1)]
one = [0,1,2,3]
two = [(0,2), (1,3)]
three = [(0,1), (1,2), (2,3), (3,0)]
four = [(3,0,1), (0,1,2), (1,2,3), (2,3,0)]
five = [(0,1,2,3)]


cctv = []
arr= []
wall = 0

for i in range(n):
    for j in range(m):
        if room[i][j] ==6:
            wall+=1
        if 0<room[i][j]<6:
            cctv.append((i,j))
            if room[i][j]==1:
                arr.append(one)
            elif room[i][j]==2:
                arr.append(two)
            elif room[i][j]==3:
                arr.append(three)
            elif room[i][j]==4:
                arr.append(four)
            elif room[i][j]==5:
                arr.append(five)



products = list(product(*arr))
Q =deque()
answer = n*m



for i in range(len(products)):
    temp = copy.deepcopy(room)
    cnt = 0
    for j in range(len(products[i])):

        if isinstance(products[i][j],int):
            arrays= [products[i][j]]
        elif isinstance(products[i][j],tuple):
            arrays= products[i][j]


        for k in arrays:
            y, x = cctv[j]
            Q.append((y, x))
            while Q:
                y, x = Q.popleft()
                ny = y + dir[k][0]
                nx = x + dir[k][1]
                if 0<= ny <n and 0<= nx<m and temp[ny][nx] != 6:
                    if temp[ny][nx] == 0:
                        temp[ny][nx] =9
                        cnt +=1
                        Q.append((ny,nx))
                    elif temp[ny][nx] == 9:
                        Q.append((ny, nx))
                    elif 0<temp[ny][nx]<6:
                        Q.append((ny, nx))

    answer = min(answer,n*m - len(cctv) - cnt -wall)


print(answer)
