import math
def count(num):
    cnt = 0
    for i in range(1, int(math.sqrt(num))+1):
        if i**2==num:
            cnt+=1
            continue
        
        if num%i==0:
            cnt+=2
    
    print(num, cnt)
    return cnt



def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        n = count(i)
        if n%2==0:
            answer+=i
        else:
            answer-=i
    
    return answer