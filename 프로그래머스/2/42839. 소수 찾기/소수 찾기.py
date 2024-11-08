import math
from itertools import *

def solution(numbers):
    def isprime(num):
        if num==1 or num==0:
            return False

        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True
    answer=set()

    for i in range(1,len(numbers)+1):
        num_perm = list(permutations(numbers,i))
        for perm in num_perm:
            number = int(''.join(perm))
            # print(number)

            if isprime(number):
                answer.add(number)

    return len(answer)