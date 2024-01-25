from collections import *
def solution(s):
    str= sorted(list(s[2:-2].split('},{')),key=len)

    answer=[]


    for i in str:

        for j in i.split(','):
            if j.isdigit() and int(j) not in answer:
                answer.append(int(j))


    
    return answer