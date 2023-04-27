
import sys
from heapq import *
n = int(input())

classes = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]

classes.sort()

room=[]
heappush(room,classes[0][1])

for i in range(1,n):
    if classes[i][0] < room[0]:
        heappush(room,classes[i][1])
    else:
        heappop(room)
        heappush(room,classes[i][1])

print(len(room))
