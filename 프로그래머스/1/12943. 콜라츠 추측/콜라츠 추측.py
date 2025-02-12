def solution(num):
    answer = -1
    
    if num!=1:
        for i in range(500):
            if num%2==0:
                num/=2
            else:
                num = num*3+1
            
            if num==1:
                answer = i+1
                break
    else:
        answer=0

    return answer