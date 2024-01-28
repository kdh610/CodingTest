import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    result =""
    answer =0
    while True:
        q,r= divmod(n,k)
        result=str(r) +result
        n=q

        if q==0:
            break

    for n in result.split('0'):
        if n=='1' or n=='':
            continue
        if is_prime(int(n)):
            answer+=1


    return answer