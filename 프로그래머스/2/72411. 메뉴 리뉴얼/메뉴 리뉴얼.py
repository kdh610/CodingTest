from itertools import *
from collections import *
def solution(orders, course):
    dict = defaultdict(list)

    for c in course:
        for order in orders:
            order = sorted(order)
            for comb in list(combinations(order,c)):
                dict[c].append(comb)


    answer= []
    for i in dict:
        count = Counter(dict[i]).most_common()

        MAX=count[0][1]
        if MAX<2:
            continue
        answer.append(''.join(count[0][0]))
        for j in range(1,len(count)):
            if count[j][1] == MAX:
                answer.append(''.join(count[j][0]))
    answer.sort()
    return answer