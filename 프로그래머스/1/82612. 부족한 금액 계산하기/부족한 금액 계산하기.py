def solution(price, money, count):
    answer = 0
    
    p = 0
    for i in range(1,count+1):
        p+= price*i
    
    if p>money:
        answer=p-money

    return answer