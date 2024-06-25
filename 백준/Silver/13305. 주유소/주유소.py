
import sys
from heapq import *

n = int(input())
length =[0]+ list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

for i,v in enumerate(price):
    price[i] = (v,i)

for i in range(1,len(length)):
    length[i] += length[i-1]

#print(length)
answer = 0

heap = price[0:n-1]
heapify(heap)
min_idx=n
end= n-1
while min_idx!=0:



    min_price, min_idx = heappop(heap)
    if min_idx < end:


        distance = length[end] - length[min_idx]
        answer += distance * min_price
        end = min_idx



print(answer)