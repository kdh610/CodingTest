from collections import *
def solution(gems):
    answer = [1,len(gems)]
    number = len(set(gems))

    start, end = 0, 0
    dict = defaultdict(int)
    dict[gems[end]]=1
    while start < len(gems) and end < len(gems):
        if len(dict)==number:
            if answer[1]-answer[0] > end-start:
                answer[0]=start+1
                answer[1]=end+1



        if len(dict) < number :

            end += 1
            if end == len(gems):
                break
            dict[gems[end]] += 1

        else:
            dict[gems[start]] -= 1
            if dict[gems[start]] == 0:
                del dict[gems[start]]

            start += 1



    print(answer)
    


    return [answer[0],answer[1]]
