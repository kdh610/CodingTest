from collections import *
def solution(k, tangerine):
    weight = sorted(Counter(tangerine).values(), reverse=True)

    s = 0
    answer = 0
    for w in weight:

        if s+w >= k:
            answer+=1
            break

        s += w
        answer += 1
    return answer