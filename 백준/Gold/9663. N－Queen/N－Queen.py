
N = int(input())


visit = [[False,-1] for _ in range(N)]
row = [-1] *N
answer = 0




def back(cnt, prev):
    global answer
    # print(cnt,'행' ,prev,'열')
    # print(visit)

    for i in range(1,cnt):
        #print('i',i)
        if (prev-i>=0 and visit[prev-i][0] and visit[prev-i][1] == cnt-i-1) or (prev+i<N and visit[prev+i][0] and visit[prev+i][1] ==  cnt-i-1):
            #print("대각")
            return

    if cnt==N:
        #print("N queen!!===============")
        answer+=1
        return

    for i in range(N):
        if (i<=prev-2 or i>=prev+2 ) and not visit[i][0]:
            visit[i][0] = True
            visit[i][1] = cnt
            back(cnt+1, i)
            visit[i][0] = False
            visit[i][1] = -1

for i in range(N):
    visit[i][0] = True
    visit[i][1] = 0
    back(1,i)
    visit[i][0] =False
    visit[i][1] = -1

print(answer)