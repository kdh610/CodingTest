def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        value = absolutes[i]
        if not signs[i]:
            value = -1 * absolutes[i]
        
        answer+=value
    
    
    return answer