

from heapq import *
from collections import *
n = int(input())

todos = []
deadline = 0

for _ in range(n):
    d,w = map(int,input().split())
    deadline = max(deadline,d)
    todos.append([d*-1,w])

todos.sort(key=lambda x: x[1])



heapify(todos)
temp = list()
answer = 0

for i in range(deadline,0,-1):
    #print('=========i',i)
    #print(todos)
    while todos:
        task = heappop(todos)
        #print('task',task)
        if task[0]*-1>=i:
            temp.append(task)
        else:
            heappush(todos,task)
            break


    temp.sort(key=lambda x: x[1])
    #print('temp',temp)
    if temp:
        task = temp.pop()
        answer+=task[1]


    for t in temp:
        heappush(todos, t)
    temp = []
    #print('ans',answer)

print(answer)




