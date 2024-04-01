import math
from itertools import *

n,k=map(int,input().split())

answer = int(math.factorial(n) // (math.factorial(n-k)*math.factorial(k))) %10007



print(answer)