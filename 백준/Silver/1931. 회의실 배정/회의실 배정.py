import sys

n=int(input())

meeting=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

meeting.sort(key=lambda x: (x[1],x[0]))
tmp=0
answer=0

for start,end in meeting:
     if start>=tmp:

         tmp=end
         answer+=1




print(answer)
