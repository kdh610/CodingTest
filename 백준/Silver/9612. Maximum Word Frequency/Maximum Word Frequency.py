from collections import *

n = int(input())

words = [input() for _ in range(n)]

counter = Counter(words).most_common()

counter.sort(key=lambda x:[x[1],x[0]], reverse=True)
print(counter[0][0]+' '+str(counter[0][1]))