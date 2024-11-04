import sys

while True:
    try:
        x = int(input())*int(1e7)
        n = int(input())
        legos =[int(sys.stdin.readline()) for _ in range(n)]

        legos.sort()

        answer = 'danger'
        left, right = 0,n-1
        l1,l2=0,0

        while left<right:

            temp = legos[left] + legos[right]
            # print('left,right',left,right)
            # print(temp)
            if temp == x:
                answer = 'yes'

                l1 = legos[left]
                l2 = legos[right]
                break
            elif temp<=x:

                left+=1
            else:
                right-=1

        if answer=='danger':
            print(answer)
        else:
            print(answer,l1,l2)
    except:
        break