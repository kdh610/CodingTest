
from collections import *
from copy import *

n = int(input())

bricks = [[0,0,0,0]]
graph = defaultdict(list)

for i in range(n):
    a, h ,w = map(int,input().split())
    bricks.append([i+1, a, h, w])

bricks.sort(key=lambda x: x[3])
#print(bricks)

dp = [0] *(n+1)
top = defaultdict(list)

for i in range(1,n+1):
    #print('----i',i)
    for j in range(0,i):
        #print('j',j)
        if bricks[i][1] > bricks[j][1]:
            if dp[i] < dp[j] + bricks[i][2]:
                dp[i]  =dp[j] + bricks[i][2]
                #print(top[j])
                top[i] = deepcopy(top[j])
                top[i].append(bricks[i][0])
                #print(top)
            #dp[i] = max(dp[i], dp[j] + bricks[i][2])

idx = 0
maxH= 0
for i in range(n+1):
    if maxH< dp[i]:
        maxH=dp[i]
        idx = i

# print(dp)
# print(top)
#
# print('idx',idx)

print(len(top[idx]))
for i in top[idx]:
    print(i)








