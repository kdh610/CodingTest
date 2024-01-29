from collections import *
def solution(N, stages):
    answer=[]
    fails=[]
    counter=Counter(stages)

    for i in range(1,N+1):
        users=0
        fail=counter[i]
        for j in range(i,N+2):
            users+=counter[j]

        if users==0:
            fails.append((0,i))
        else:
            fails.append((fail/users, i))

    fails.sort(key=lambda x:[-x[0],x[1]])

    for i in fails:
        answer.append(i[1])
    return answer