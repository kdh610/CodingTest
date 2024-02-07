from collections import *
import sys

N,M = map(int, input().split())

no_listen = defaultdict(bool)
answer = []

for i in range(N):
    name = sys.stdin.readline().strip()
    no_listen[name]=True

for i in range(M):
    name = sys.stdin.readline().strip()
    if no_listen[name]:
        answer.append(name)

answer.sort()
print(len(answer))
for n in answer:
    print(n)

