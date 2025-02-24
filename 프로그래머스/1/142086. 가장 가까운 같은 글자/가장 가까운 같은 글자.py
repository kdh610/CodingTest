from collections import *
def solution(s):
    answer = []
    
    alpha_dict = dict()


    for i in range(len(s)):
        if s[i] not in alpha_dict.keys():
            alpha_dict[s[i]] = i


    for i in range(len(s)):
        if s[i] in alpha_dict.keys():
            result = i - alpha_dict[s[i]]

            if result==0:
                answer.append(-1)
            else:
                answer.append(result)
                alpha_dict[s[i]] = i

    
    
    return answer