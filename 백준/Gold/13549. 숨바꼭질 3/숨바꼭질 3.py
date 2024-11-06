from collections import *

n,k = map(int,input().split())
visit = [False]*100001
point = [0]*100001
Q = deque()

Q.append(n)
visit[n] = True

while Q:
    cur = Q.popleft()
    # print('cur',cur)
    for n_cur in [cur-1, cur+1, cur*2]:
        # print(n_cur)
        if 0<= n_cur <= 100000 and not visit[n_cur]:
            if n_cur==cur*2:
                Q.appendleft(n_cur)
                point[n_cur] = point[cur]
                visit[n_cur]=True
            else:
                Q.append(n_cur)
                visit[n_cur]=True
                point[n_cur] = point[cur]+1

# print(point[:k])
print(point[k])