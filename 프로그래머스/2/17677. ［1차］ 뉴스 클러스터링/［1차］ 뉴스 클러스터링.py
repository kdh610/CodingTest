import copy

def solution(str1, str2):
    answer=0
    str1=str1.lower()
    str2=str2.lower()

    set1=[]
    set2=[]

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i] + str1[i+1])

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i] + str2[i+1])

    inter =[]
    union = set1.copy()
    set1_temp = set1.copy()
    

    for i in set2:
        if i not in set1_temp:
            union.append(i)
        else:
            set1_temp.remove(i)

    for i in set2:
        if i in set1:
            set1.remove(i)
            inter.append(i)
    if len(union)==0:
        answer=65536
    else:
        answer=int((len(inter)/len(union))*65536)

    return answer