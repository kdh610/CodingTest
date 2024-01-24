from collections import *
def solution(cacheSize, cities):
    cach=deque()
    answer = 0
    if cacheSize==0:
            return len(cities)*5
    for city in cities:
        s = city.lower()
        if s not in cach and len(cach)<cacheSize:
            cach.append(s)
            answer+=5
        else:
            if s not in cach:
                cach.popleft()
                cach.append(s)
                answer+=5
            else:
                cach.remove(s)
                cach.append(s)
                answer+=1
    return answer