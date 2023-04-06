from collections import *
from heapq import *
def solution(cacheSize, cities):
    answer = 0
    cache = deque() 
    heap = []
    
    if cacheSize==0:
        return len(cities)*5
    
    
    for city in cities:
        if len(cache)<cacheSize and city.lower() not in cache:
            cache.append(city.lower())
            answer+=5
            
        else:
            if city.lower() not in cache:
                cache.popleft()
                cache.append(city.lower())
                answer+=5
            else:
                cache.remove(city.lower())
                cache.append(city.lower())
                answer+=1
    
    return answer