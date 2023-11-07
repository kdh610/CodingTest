import sys


length,width,height = map(int,input().split())
n=int(input())

cube=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

volume = length*width*height
answer=0
cube.sort(reverse=True)
prev=0

for i,total in cube:

    prev *=  8
    len = 2**i

    cnt=(length//len) * (width//len) * (height//len)

    answer+=min(cnt-prev,total)
    prev+=min(cnt-prev,total)






if volume==prev:
    print(answer)
else:
    print(-1)