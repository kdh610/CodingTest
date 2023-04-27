
import sys
n,k = map(int,input().split())

coin = [ int(input()) for _ in range(n)]

coin.sort(reverse=True)
answer=0
for c in coin:
    answer += k // c
    k=k%c



print(answer)