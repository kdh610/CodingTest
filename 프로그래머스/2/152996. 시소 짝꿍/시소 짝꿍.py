
from collections import *
import math

def solution(weights):
    count = Counter(weights)
    dict = defaultdict(list)


    for i in range(100,4001):
        for j in range(2,5):
            if float(i/j).is_integer():
                dict[i].append(int(i/j))


    answer = 0

    for c in count:

        if count[c]>=2:
            answer += math.comb(count[c],2)

            

        for i in [2,3,4]:

            for j in dict[c*i]:

                if j==c:
                    continue
                if count[j]>0 and c<j:
                    answer += count[c] * count[j]

    return answer