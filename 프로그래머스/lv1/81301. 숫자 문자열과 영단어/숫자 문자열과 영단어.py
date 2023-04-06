from collections import *
def solution(s):
    answer = ""
    dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    start = 0
    for i in range(len(s)+1):
        number = s[start:i]
        # print(number)
        if number.isdigit():
            answer += number
            start+=1
            # print(f'{answer=}')
        elif number in dict:
            answer += dict[number]
            start=i
            # print(f'{number=}')
            # print(f'{answer=}')
            
        
    

    
    
    return int(answer)