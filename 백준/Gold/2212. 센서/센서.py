import sys

n=int(input())
k=int(input())
sensor=list(map(int,sys.stdin.readline().split()))

distance=[0]

sensor.sort()

for i in range(1,n):
    distance.append(abs(sensor[i]-sensor[i-1]))


answer=sensor[-1]-sensor[0]

distance.sort(reverse=True)

for i in range(len(distance)):
    if i==k-1:
        break
    answer-=distance[i]
print(answer)


