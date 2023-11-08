n = int(input())
candy =[list(input()) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0
temp = ''
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = dx[k] + j
            ny = dy[k] + i
            if nx>=0 and ny>=0 and nx<n and ny<n:
                
                if candy[i][j] != candy[ny][nx]:
                    temp = candy[i][j]
                    candy[i][j] = candy[ny][nx]
                    candy[ny][nx] = temp
                    
                row_cnt = 1;
                col_cnt = 1;
                for l in range(n-1):
                    if candy[i][l] == candy[i][l+1]:
                        row_cnt +=1
                    else:
                        row_cnt = 1
                    if candy[l][j] == candy[l+1][j]:
                        col_cnt += 1
                    else:
                        col_cnt=1
                    result = max(result, row_cnt, col_cnt)
                    
                if candy[i][j] != candy[ny][nx]:
                    candy[ny][nx] = candy[i][j]
                    candy[i][j] = temp

print(result)

