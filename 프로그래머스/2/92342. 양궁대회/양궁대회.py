from itertools import *
from collections import *
def solution(n, info):
    apeach = defaultdict(int)

    for i in range(len(info)):
        apeach[10-i] = info[i]

    arr = [0,1,2,3,4,5,6,7,8,9,10]

    score_gap = 0
    ans = [-1]
    for comb in (list(combinations_with_replacement(arr,n))):
        ryan = Counter(comb)
        aScore =0
        rScore = 0

        for i in range(11):
            if ryan[i]==0 and apeach[i]==0: continue

            if ryan[i]>apeach[i]:
                rScore+=i
            else:
                aScore+=i

        if rScore>aScore:
            gap = rScore-aScore
            if score_gap<gap:
                score_gap = gap
                ans = ryan
                #print(score_gap)
            elif score_gap==gap:
                #print('ans',answer)
                #print('ryan',ryan)
                for i in range(10):
                    if ryan[i]>ans[i]:
                        ans = ryan
                        break
                    else:
                        break

    answer = [0]*11

    if ans==[-1]:
        answer = ans
    else:
        for i in range(11):
            answer[10-i] = ans[i]
    return answer