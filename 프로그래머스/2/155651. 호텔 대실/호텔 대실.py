
from heapq import *

def solution(book_time):
    book_time.sort()
    heap = []

    print(book_time)
    last = -1
    cnt= 0
    for time in book_time:
        start_hour = time[0].split(':')[0]
        start_min = time[0].split(':')[1]
        end_hour = time[1].split(':')[0]
        end_min = time[1].split(':')[1]


        start = 60*int(start_hour) + int(start_min)
        end = 60 * int(end_hour) + int(end_min)

        if heap:
            last = heappop(heap)
            if last+10<=start:
                heappush(heap,end )
            else:
                heappush(heap, end )
                cnt+=1
                heappush(heap,last)
        else:
            heappush(heap, end)
            cnt += 1

    return cnt