

n,l = map(int,input().split())

field = [list(map(int,input().split())) for _ in range(n)]
field_col = list(zip(*field))


answer = 0

check_row = [[False]*n for _ in range(n)]
check_col = [[False]*n for _ in range(n)]

def slope(field,check):
    global answer
    for i in range(n):
        temp = field[i][0]
        cnt = 101
        for j in range(1,n):
            if cnt < l:
                cnt+=1
                check[i][j-1]=True


            if abs(temp - field[i][j]) >1:
                break
            else:
                if temp>field[i][j]:
                    arr = set(field[i][j:j+l])
                    if len(field[i][j:j+l])!=l or len(arr)>1 or True in check[i][j:j+l]:
                        break
                    cnt=0

                elif temp<field[i][j]:
                    arr = set(field[i][j-l:j])
                    if len(field[i][j-l:j])!=l or len(arr) > 1 or True in check[i][j-l:j]:
                        break
            temp= field[i][j]
        else:
            answer+=1

slope(field,check_row)
slope(field_col,check_col)


print(answer)


