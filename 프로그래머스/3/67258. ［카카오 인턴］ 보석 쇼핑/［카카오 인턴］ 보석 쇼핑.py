from collections import *
def solution(gems):
    total_gem = len(set(gems))

    left = 0
    right = 0
    gem_cnt = defaultdict(int)

    gem_cnt[gems[left]]+=1
    start,end=1,len(gems)

    while left < len(gems) and right < len(gems):

        if len(gem_cnt)==total_gem:
            if end-start > right-left:
                start=left+1
                end=right+1
                print('start,end',start,end)

        if len(gem_cnt)<total_gem:
            right+=1
            if right>=len(gems):
                break

            gem_cnt[gems[right]] += 1



        else:
            gem_cnt[gems[left]] -= 1
            if gem_cnt[gems[left]] == 0:
                del gem_cnt[gems[left]]
            left += 1


    return [start,end]
