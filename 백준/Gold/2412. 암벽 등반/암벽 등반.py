
from collections import *

n, T = map(int, input().split())

point= []
graph = defaultdict(list)

for i in range(n):
    x, y = map(int,input().split())
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

#print(graph)

def bfs():
    Q = deque()

    Q.append((0, 0))
    ans = 0
    while Q:
        size = len(Q)
        for _ in range(size):
            x,y = Q.popleft()
            #print('x,y',x,y)
            if y==T:
                return ans

            for i in range(y-2, y+3):
                if i<0 or i>200000:
                    continue
                #print('i',i)
                remove_list = []
                for j in range(len(graph[i])):
                    #print('j',j)
                    #print(graph[i][j])
                    if x+2 < graph[i][j]:
                        break
                    elif x-2 > graph[i][j]:
                        continue
                    Q.append((graph[i][j],i))
                    #print(Q)
                    remove_list.append(graph[i][j])

                for k in remove_list:
                    graph[i].remove(k)

        ans+=1
    return -1
print(bfs())









