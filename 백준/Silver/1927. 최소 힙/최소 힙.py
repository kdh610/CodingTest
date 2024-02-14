import heapq


import sys

N = int(input())
heap=[]

for _ in range(N):
    number = int(sys.stdin.readline().strip())

    if number<=0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,number)
