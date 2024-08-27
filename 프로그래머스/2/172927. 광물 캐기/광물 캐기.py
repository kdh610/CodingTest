import math
from collections import *
def solution(picks, minerals):

    total_mineral = min(sum(picks)*5, len(minerals))

    diacnt = 0
    ironcnt =0
    stonecnt = 0
    split_minerals = []


    for i in range(total_mineral):

        if minerals[i] == 'diamond':
            diacnt+=1
        elif minerals[i] == 'iron':
            ironcnt+=1
        else:
            stonecnt+=1

        if (i+1)%5==0 or i==total_mineral-1:
            split_minerals.append((diacnt, ironcnt, stonecnt))
            diacnt=0
            ironcnt=0
            stonecnt=0



    split_minerals.sort(key=lambda x: [x[0], x[1], x[2]], reverse=True)

    answer = 0

    for mineral in split_minerals:
        pick = -1

        if picks[0]>0:
            pick = 0
            picks[0]-=1
        elif picks[1]>0:
            pick = 1
            picks[1] -= 1
        elif picks[2]>0:
            pick = 2
            picks[2] -= 1

        if pick==0:
            answer += mineral[0] + mineral[1] + mineral[2]
        elif pick == 1:
            answer += mineral[0]*5 + mineral[1] + mineral[2]
        elif pick == 2:
            answer += mineral[0] * 25 + mineral[1]*5 + mineral[2]


    return answer
