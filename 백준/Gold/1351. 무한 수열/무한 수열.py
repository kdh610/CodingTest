from collections import *
import math

N,P,Q = map(int,input().split())

result = defaultdict(int)
result[0] =1

def dp(start):
    if start ==0:
        return 1
    if result[start]: return result[start]

    result[start] = dp(start//P) + dp(start//Q)
    return result[start]

dp(N)
print(result[N])