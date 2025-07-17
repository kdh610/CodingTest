from itertools import *
from collections import *
def solution(dice):
    n = len(dice)
    dice_num = {i for i in range(n)}
    answer = []
    max_win = 0
    for comb in combinations(dice_num,n//2):
        A_comb = set(comb)
        A_dice = [dice[i] for i in A_comb]
        A_score = defaultdict(int)
        for s in list(product(*A_dice)):
            A_score[sum(s)]+=1

        B_comb = dice_num - A_comb
        B_dice = [dice[i] for i in B_comb]
        B_score=defaultdict(int)
        for s in list(product(*B_dice)):
            B_score[sum(s)]+=1


        presum= [0] * 501
        s = 0
        for i in range(1,501):
            if i in B_score:
                s+=B_score[i]
            presum[i]=s



        win = 0
        for i,v in A_score.items():
            win += presum[i-1]*v

        if win>max_win:
            max_win = win
            answer = comb

    return [i+1 for i in answer]