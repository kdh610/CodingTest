from collections import *

dy = [0,0,1,-1]
dx = [1,-1,0,0]
def bfs(place):
    for i in range(5):
        for j in range(5):
            Q = deque()
            visit = [[False] * 5 for _ in range(5)]
            if place[i][j] == 'P':
                Q.append((i, j))
                visit[i][j] = True
                distance = 0
                while Q:
                    distance += 1
                    cnt = len(Q)
                    for k in range(cnt):
                        y, x = Q.popleft()
                        for a in range(4):
                            ny = y + dy[a]
                            nx = x + dx[a]
                            if 0 <= ny < 5 and 0 <= nx < 5 and not visit[ny][nx] and place[ny][nx] != 'X':
                                if place[ny][nx] == 'P':

                                    return False
                                if distance <= 1:
                                    visit[ny][nx] = True
                                    Q.append((ny, nx))
    return True

def solution(places):

    answer=[]
    for p in range(len(places)):
        place = places[p]
        flag = bfs(place)
        if not flag:
            answer.append(0)
        else:
            answer.append(1)
    return answer