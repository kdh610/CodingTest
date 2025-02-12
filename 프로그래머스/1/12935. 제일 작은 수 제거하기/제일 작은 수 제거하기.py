def solution(arr):
    answer = []
    
    if len(arr)==1:
        return [-1]
    
    min_val = min(arr)
    
    arr.remove(min_val)
    
    
    return arr