from collections import *
def solution(id_list, report, k):
    complaint = defaultdict(set)
    complain_count = defaultdict(int)
    mail = defaultdict(int)

    for r in report:
        fr, to = r.split(" ")
        if to in complaint[fr]:
            continue
        complain_count[to]+=1
        complaint[fr].add(to)


    for key,value in complain_count.items():
        if value >=k:
            for user in id_list:
                if key in complaint[user]:
                    mail[user]+=1

    answer=[]
    for i in id_list:
        answer.append(mail[i])
    return answer