from collections import *
def solution(n, wires):
    graph = [[] for _ in range(n+1)]

    for wire in wires:
        a,b = wire
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start,visit):
        Q= deque()
        Q.append(start)
        visit[start]=True
        cnt=1
        while Q:
            top = Q.popleft()
            for t in graph[top]:
                if not visit[t]:
                    visit[t]=True
                    cnt+=1
                    Q.append(t)
        return cnt

    answer=int(1e9)

    for wire in wires:
        a,b = wire
        graph[a].remove(b)
        graph[b].remove(a)

        visit = [False]*(n+1)

        cnt1 = bfs(a,visit)
        cnt2 = bfs(b,visit)

        if abs(cnt1-cnt2) < answer:
            answer=abs(cnt1-cnt2)

        graph[a].append(b)
        graph[b].append(a)
    return answer