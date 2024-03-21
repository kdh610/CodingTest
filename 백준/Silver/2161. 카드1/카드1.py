

from collections import *


N = int(input())
cards = deque()
for i in range(1,N+1):
    cards.append(i)

answer = []

while cards:
    first = cards.popleft()
    answer.append(first)

    if cards:
        second = cards.popleft()
        cards.append(second)

print(*answer)