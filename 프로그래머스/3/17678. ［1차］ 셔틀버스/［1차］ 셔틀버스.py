from collections import *
from heapq import *

def solution(n, t, m, timetable):
    answer = ''
    depart = []
    dict = defaultdict(list)
    time = 9 * 60

    for i in range(n):
        depart.append(time)
        dict[time]
        time += t
        
    print(depart)

    for i in range(len(timetable)):
        hour, minnute = timetable[i].split(':')
        timetable[i] = int(hour) * 60 + int(minnute)
        
    heapify(timetable)

    print(timetable)

    for i in range(len(depart)):
        cnt=0
        while timetable and cnt<int(m):
            person = heappop(timetable)
            if person<=depart[i]:
                dict[depart[i]].append(person)
                cnt+=1
            else:
                heappush(timetable,person)
                break
    print(dict)
    bus = list(dict.keys())[-1]
    print(len(dict[bus]))
    
    if len(dict[bus]) < int(m):
        if len(dict[bus])==0:
            answer=bus
        else:
            answer=bus
    else:
        if len(dict[bus])==0:
            answer=dict[bus]
        else:
            answer=dict[bus][-1]-1
    hour= str(answer//60)
    minute = str(answer%60)
    if len(hour)<2:
        hour='0'+hour
    if len(minute)<2:
        minute='0'+minute
    answer = hour+':'+minute
    return answer