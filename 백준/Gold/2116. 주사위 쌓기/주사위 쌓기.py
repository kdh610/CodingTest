

import sys

n = int(input())


dice = []


for _ in range(n):
    dice.append(list(map(int,sys.stdin.readline().split())))


def set_bottom(arr,num):
    bottom = 5
    top = 0
    for i in range(6):
        if arr[i] == num:
            bottom = i
            if bottom== 1:
                top = 3
            elif bottom==3:
                top = 1
            elif bottom==2:
                top=4
            elif bottom==4:
                top=2

            arr[5], arr[bottom] = arr[bottom], arr[5]
            arr[0], arr[top] = arr[top], arr[0]
            # print(arr)
            break

answer = n

for i in range(1,7):
    # print('bot:',dice[0][5], ' top:',dice[0][0])
    set_bottom(dice[0], i)
    temp = 0
    for j in range(1, n):
        set_bottom(dice[j], dice[j-1][0])

    # print(dice)
    for k in range(n):
        temp += max(dice[k][1:5])

    answer=max(answer,temp)

print(answer)

