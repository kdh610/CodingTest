def solution(phone_number):
    answer = ''
    
    length = len(phone_number)
    
    front = '*' * (length-4)
    
    answer = front +phone_number[length-4:]
    
    return answer