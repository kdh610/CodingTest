import sys
n = int(input())

meeting = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]

meeting.sort(key=lambda x:[x[1],x[0]])

cnt=1
end = meeting[0][1]

for i in range(1,n):
    if meeting[i][0] >= end:
        cnt +=1
        end = meeting[i][1]

print(cnt)