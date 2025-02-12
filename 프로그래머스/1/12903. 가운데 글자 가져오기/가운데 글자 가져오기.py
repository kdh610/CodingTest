def solution(s):
    answer = ''
    
    length = len(s)
    
    idx = length//2
    
    if length%2==1:
        answer = s[idx]
    else:
        answer = s[idx-1] + s[idx]
    
    
    return answer