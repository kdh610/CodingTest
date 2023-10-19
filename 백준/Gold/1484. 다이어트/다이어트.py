import math

G = int(input())



answer = []
left, right =1,1



while left<=right:

    dif = right**2 - left**2
    if right - left == 1 and dif > G:
        break
    if dif < G:
        right+=1
    elif dif > G:
        left +=1
    elif dif==G:
        answer.append(right)
        left+=1

if len(answer)==0:
    print(-1)
else:
    for i in answer:
            print(int(i))








