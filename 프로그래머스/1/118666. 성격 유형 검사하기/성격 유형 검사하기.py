
from collections import *
def solution(survey, choices):
    score = [0,3,2,1,0,1,2,3]
    mbti = defaultdict(int)

    for i in range(len(survey)):
        choice = choices[i]
        s = survey[i]
        if 1<=choice<=3:
            mbti[s[0]]+=score[choice]
        elif 5<=choice<=7:
            mbti[s[1]] += score[choice]

    answer=''
    def choice(a,b,answer):
        if mbti[a]>mbti[b]:
            answer+=a
        elif mbti[a]<mbti[b]:
            answer+=b
        else:
            answer += a
        return answer
    answer =choice('R','T',answer)
    answer =choice('C','F',answer)
    answer =choice('J','M',answer)
    answer=choice('A','N',answer)
    
    return answer