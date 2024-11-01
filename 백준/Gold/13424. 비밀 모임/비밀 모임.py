


T = int(input())


for t in range(T):

    n,m = map(int,input().split())

    room = [[int(1e9)]*(n+1) for _ in range(n+1)]

    for i in range(m):
        a,b,c=map(int,input().split())
        room[a][b]=c
        room[b][a]=c

    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                room[i][j]=0

    k = int(input())
    friend = list(map(int,input().split()))

    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):

                room[a][b] = min(room[a][b], room[a][k]+room[k][b])


    # print(*room,sep='\n')

    min_dist=int(1e9)
    answer = 0
    for i in range(1,n+1):
        dist = 0
        for j in friend:
            dist+=room[j][i]

        if min_dist > dist:
            min_dist=dist
            answer=i
            


    print(answer)







