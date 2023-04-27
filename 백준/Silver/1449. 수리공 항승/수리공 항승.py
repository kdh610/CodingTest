
import sys
n,l = map(int,input().split())

leak = list(map(int,sys.stdin.readline().split()))

leak.sort()

cnt=1
tape = leak[0]-0.5 + l

for i in leak:
    if i > tape:
        cnt+=1
        tape = i-0.5 +l


print(cnt)
