from collections import *
import sys
a, b = map(int,input().split())

set_a = list(map(int,sys.stdin.readline().split()))
set_b = list(map(int,sys.stdin.readline().split()))


print(len(Counter(set_a) | Counter(set_b)) - len(Counter(set_a) & Counter(set_b)))