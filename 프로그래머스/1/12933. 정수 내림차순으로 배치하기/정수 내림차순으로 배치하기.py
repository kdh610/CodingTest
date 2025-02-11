def solution(n):
    answer = 0
    
    arr = list(str(n))
    arr.sort(reverse=True)

    
    answer =int(''.join(arr))
    
    return answer