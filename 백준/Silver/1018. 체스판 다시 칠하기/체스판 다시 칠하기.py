import sys


n,m = map(int,input().split())

board = [sys.stdin.readline().strip() for _ in range(n)]
answer=64
for i in range(n):
    for j in range(m):

        if i+7 <=n-1 and j+7<=m-1:

            tmp = [board[k][j:j+8] for k in range(i,i+8)]
            cnt=0

            for r in range(8):
                for c in range(8):
                    if r%2==0:
                        if c%2==0 and tmp[r][c] == 'W':
                            cnt += 1
                        if c%2==1 and tmp[r][c]=='B':
                            cnt+=1
                    else:

                        if  c%2==0 and tmp[r][c] == 'B':
                            cnt += 1
                        if c%2==1 and tmp[r][c]=='W':
                            cnt+=1

            answer=min(answer,cnt,64-cnt)

print(answer)
