N = int(input())


visit = [False] * (N+1)
result=[]




def permutation(cnt):

    if cnt==N:
        print(*result)
        return


    for i in range(1,N+1):

        if not visit[i]:
            visit[i]=True
            result.append(i)
            permutation(cnt+1)
            result.pop()
            visit[i]=False




permutation(0)