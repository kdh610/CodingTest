from itertools import *
def solution(k, dungeons):
    answer = 0
    for i in list(permutations(dungeons)):
        tired = k
        cnt=0

        for j in i:
            if j[0]>tired:
                continue

            tired-=j[1]
            cnt+=1

        answer=max(answer,cnt)
    return answer