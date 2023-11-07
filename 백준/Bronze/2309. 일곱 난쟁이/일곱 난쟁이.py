import sys


height=[int(input()) for _ in range(9)]




sum=sum(height)


for i in range(8):

    a=height[i]
    for j in range(i+1,9):

        b=height[j]

        if a+b == sum-100:
            height.remove(a)
            height.remove(b)
            break
    if a + b == sum - 100:
        break

height.sort()

for i in height:
    print(i)