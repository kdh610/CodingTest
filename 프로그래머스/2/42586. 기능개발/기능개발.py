import math
def solution(progresses, speeds):
    remain = [0]

    for i in range(len(progresses)):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))

    cnt = 0
    prev = remain[0]
    answer = []
    for i in range(1,len(remain)):
        cur = remain[i]
        if cur <= prev:
            cnt+=1

        else:
            answer.append(cnt)
            prev = cur
            cnt=1
        if i == len(remain) - 1:
            answer.append(cnt)
    return answer[1:]