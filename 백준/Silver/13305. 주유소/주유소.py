
import sys

n = int(input())
length = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

answer = 0

def find_min(price, start, end):
    global answer
    min_price = min(price[start:end])
    min_idx = price.index(min_price)

    distance = sum(length[min_idx:end])
    answer += distance * min_price

    if min_idx!=0:
        find_min(price, 0, min_idx)


find_min(price,0,n)

print(answer)





