
n,m = map(int,input().split())

arr = [list(input()) for _ in range(n)]

def sqrt(result):
    result = int(result)
    if int(result**0.5) ** 2 == result:
        return True

answer = -1
for i in range(n):
    for j in range(m):
        for row_dif in range(-n,n):
            for col_dif in range(-m,m):
                row, col = i,j
                result = ''
                if row_dif==0 and col_dif==0: continue
                while 0<=row<n and 0<=col<m:
                    result+=arr[row][col]

                    if sqrt(result):
                        answer=max(answer,int(result))

                    row+=row_dif
                    col+=col_dif


print(answer)