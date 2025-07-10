from collections import *
def solution(want, number, discount):
    dict = defaultdict()

    for i in range(len(want)):
        dict[want[i]] = number[i]


    answer = 0

    for i in range(len(discount)):

        counter = Counter(discount[i:i+10])
        check = True

        for item in want:
            if dict[item] != counter[item]:
                check = False
                break

        if check:
            answer+=1
    return answer