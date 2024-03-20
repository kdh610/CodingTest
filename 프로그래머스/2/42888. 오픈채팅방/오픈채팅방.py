from collections import *
def solution(record):
    user = defaultdict()

    for i in record:
        info = i.split(" ")
        if info[0]=="Enter" or info[0]=="Change":
            user[info[1]] = info[2]

    result=[]

    for i in record:

        info = i.split(" ")
        if info[0] == "Enter":
            result.append(user[info[1]]+"님이 들어왔습니다.")
            #print(user[info[1]]+"님이 들어왔습니다.")
        elif info[0] == "Leave":
            result.append(user[info[1]]+"님이 나갔습니다.")
            #print(user[info[1]]+"님이 들어왔습니다.")

    return result