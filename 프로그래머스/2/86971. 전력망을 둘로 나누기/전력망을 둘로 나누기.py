from collections import *
def solution(n, wires):
    answer = int(1e9)
    graph = defaultdict(list)

    for wire in wires:
        s = wire[0]
        e = wire[1]
        graph[s].append(e)
        graph[e].append(s)


    def bfs(start, end):

        Q = deque()
        Q.append(start)
        visit = [False] * (n+1)
        visit[start] = True
        cnt =1

        while Q:
            x = Q.popleft()
            for v in graph[x]:
                if v == end:
                    continue

                if not visit[v]:
                    visit[v]=True
                    cnt+=1
                    Q.append(v)
        return cnt


    for wire in wires:
        s = wire[0]
        e = wire[1]

        cnt1= bfs(s,e)
        cnt2 = bfs(e,s)


        result  = abs(cnt1-cnt2)

        answer = min(answer,result)

    return answer