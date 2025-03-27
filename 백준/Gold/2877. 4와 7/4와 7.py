from itertools import *

k = int(input())

arr = [4,7]
length=1
while True:

    if k - (2**length)>0:
        k = k - (2 ** length)
        length+=1
        continue

    else:
        break


binary = bin(k - 1)[2:].zfill(length)
print(binary.replace('0','4').replace('1','7'))