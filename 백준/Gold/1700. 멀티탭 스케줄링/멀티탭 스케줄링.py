import sys
from collections import *
from heapq import *

n,k = map(int,input().split())
electrics=list(map(int,sys.stdin.readline().split()))

multitab=set()
detach = set()
answer=0

for i,v in enumerate(electrics):

    if len(multitab)<n:
        multitab.add(v)
    else:
        if v not in multitab:
            for j,v2 in enumerate(electrics[i:]):

                if v2 in detach:
                    detach.remove(v2)
                if len(detach)==1:
                    break
            remove=detach.pop()


            answer+=1

            multitab.remove(remove)
            multitab.add(v)


    detach=multitab.copy()



print(answer)






