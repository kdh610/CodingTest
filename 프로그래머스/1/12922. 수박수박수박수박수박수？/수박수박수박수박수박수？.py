def solution(n):
    answer = ''
    
    soo =True
    
    for i in range(n):
        if soo:
            answer+='수'
            soo=False
        else:
            answer+='박'
            soo=True
    
    
    return answer