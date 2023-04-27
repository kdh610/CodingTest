
import sys

case = 1
while True:
    l,p,v = map(int,sys.stdin.readline().split())
    answer = 0

    if l==0 and p==0 and v==0:
        break

    answer+= (v//p)*l

    if v%p > l:
        answer += l
    else:
        answer += v%p

    print("Case " + str(case)+": "+str(answer))
    case += 1
