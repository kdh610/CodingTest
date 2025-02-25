def solution(food):
    first = ''
    answer = ''
    for i in range(1,len(food)):
        cnt = food[i] //2
        
        first+= str(i) * cnt
    
    second = first[::-1]
    print(second)
    
    answer = first+"0"+second
    
    return answer