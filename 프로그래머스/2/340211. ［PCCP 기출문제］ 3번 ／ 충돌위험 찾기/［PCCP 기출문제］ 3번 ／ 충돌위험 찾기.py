
from collections import *

t=0
def solution(points, routes):
    time = defaultdict(list)
    global t

    def route(s, e, cnt):
        global t
        start = points[s]
        end = points[e]

        start_y, start_x = start[0] - 1, start[1] - 1
        end_y, end_x = end[0] - 1, end[1] - 1


        if cnt<2:
            time[t].append((start_y, start_x))

        dir = 0
        if start_y < end_y:
            dir = 1
        elif start_y > end_y:
            dir = -1
        tmp = start_y
        for i in range(abs(start_y - end_y)):
            t += 1
            tmp += dir
            time[t].append((tmp, start_x))

        if start_x < end_x:
            dir = 1
        elif start_x > end_x:
            dir = -1
        tmp = start_x
        for j in range(abs(start_x - end_x)):
            t += 1
            tmp += dir
            time[t].append((end_y, tmp))




    for r in routes:

        t=0
        for i in range(1,len(r)):
            start = r[i-1]-1
            end = r[i]-1

            route(start,end, i)



    answer=0


    for i in time.values():

        for j in Counter(i).values():

            if j>1:
                answer+=1
    return answer