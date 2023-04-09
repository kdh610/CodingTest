from collections import *

gear= []

# rotae 사용 위해 톱니를 deque로 설정
for _ in range(4):
    gear.append(deque(input()))

n = int(input())

rotation = []

for i in range(n):
    number, dir = map(int,input().split())
    rotation.append((number-1,dir))


answer = 0
score =[1,2,4,8]

for i in rotation:
    state = [0] * 4
    number, dir = i
    temp = number
    state[number] = dir

    # 왼쪽
    while temp>0:
        if state[temp] !=0:
            if gear[temp][6] != gear[temp-1][2]:
                state[temp-1] = state[temp] * (-1)
            else:
                state[temp - 1] = 0
        else:
            state[temp-1] = 0

        temp-=1


    # 오른쪽
    while number < 3:
        if state[number] != 0:
            if gear[number][2] != gear[number + 1][6]:
                state[number + 1] = state[number] * (-1)
            else:
                state[number + 1] = 0
        else:
            state[number + 1] = 0
        number += 1

    for i,v in enumerate(state):
        # 시계방향
        if v==1:
            gear[i].rotate(1)
        #반시계
        elif v==-1:
            gear[i].rotate(-1)


for i in range(4):
    if gear[i][0]=='1':
        answer += score[i]

print(answer)











