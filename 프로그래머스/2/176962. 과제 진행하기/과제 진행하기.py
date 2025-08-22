from collections import *

def solution(plans):
    new_plan = []
    dict = defaultdict()

    for p in plans:
        subject = p[0]
        start = int(p[1].split(":")[0])*60 + int(p[1].split(":")[1])
        time = int(p[2])
        dict[subject] = time
        new_plan.append([start, time, subject])
    new_plan.sort()

    answer = []
    stack = deque()

    for i, plan in enumerate(new_plan):
        cur = plan[0]
        name = plan[2]
        time = dict[name]

        if i + 1 < len(new_plan):
            if cur+time > new_plan[i+1][0]:
                stack.append(name)
                dict[name] -= new_plan[i+1][0] - cur
                continue

            else:
                answer.append(name)
                cur = cur + time
        else:
            answer.append(name)


        while stack:
            if i + 1 < len(new_plan):
                if cur + dict[stack[-1]] <= new_plan[i+1][0]:
                    name = stack.pop()
                    answer.append(name)
                    cur = cur + dict[name]
                else:
                    dict[stack[-1]] -= new_plan[i+1][0] - cur
                    break
            else:
                answer.append(stack.pop())
                cur = cur + time
    return answer