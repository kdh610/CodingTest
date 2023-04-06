from collections import *
def solution(s):
    answer = []
    list = []
    s=s.replace("{","")
    s=s.replace("}","")
    s=s.split(',')

    for i in s:
        if i.isdigit():
            list.append(int(i))

    
    count =Counter(list).most_common()
    for i in count:
        answer.append(i[0])
    
    return answer