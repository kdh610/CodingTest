from itertools import *
from collections import *

def solution(orders, course):
    course_dict = defaultdict(list)
    course_len = [0]*11
    course_dish = defaultdict(list)

    for c in course:

        for order in orders:

            for comb in list(combinations(order,c)):
                tmp = sorted(comb)

                course_dict[c].append(tuple(tmp))
                # if course_dict[comb] > course_len[c]:
                #     course_len[c] = course_dict[comb]

    answer=[]
    for k in course_dict:


        counter = Counter(course_dict[k]).most_common()
        max_val = 0
        for key,cnt in counter:
            if cnt<=1: break
            if max_val<=cnt:
                max_val=cnt
                answer.append(''.join(key))

    answer = sorted(answer)
    return answer