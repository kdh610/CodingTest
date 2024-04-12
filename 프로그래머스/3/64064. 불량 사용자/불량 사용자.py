from collections import *
from itertools import *

def solution(user_id, banned_id):
    user_comb = list(permutations(user_id, len(banned_id)))

    ban_set=set()

    for user in user_comb:
        next= False
        compare = list(zip(user,banned_id))

        for c in compare:
            id,pattern = c[0],c[1]

            if len(id)!=len(pattern):
                next = True
                break
            for i in range(len(id)):
                if pattern[i]!='*' and id[i]!=pattern[i]:
                    next = True
                    break
            if next: break

        if next:
            continue
        else:
            user=sorted(list(user))
            ban_set.add(tuple(user))


    return len(ban_set)