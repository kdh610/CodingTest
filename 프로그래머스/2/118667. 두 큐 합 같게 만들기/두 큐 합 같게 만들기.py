from collections import *

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    total = (len(queue1) + len(queue2))*2

    sum1= sum(queue1)
    sum2 = sum(queue2)
    cnt=0

    # if (sum1+sum2)%2==0:

    while True:
        if cnt>total:
            cnt=-1
            break
        if sum1==sum2: break

        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num
        cnt+=1
    return cnt