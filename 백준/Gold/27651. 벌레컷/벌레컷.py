
import sys

N = int(input())

bug = list(map(int,sys.stdin.readline().split()))


sum = [0] * N
sum[0] = bug[0]
for i in range(1,N):
    sum[i] = sum[i-1] + bug[i]

answer=0
l = 1
r = N-2
for i in range(N):

    head = sum[i]
    l = max(l,i+1)
    while r>0 and sum[N-1] - sum[r] <= head:
        r-=1

    while l<N-1 and sum[l]-head <= sum[N-1] - sum[l]:
        l+=1

    if l>r: break

    answer+= r-l+1;


print(answer)
