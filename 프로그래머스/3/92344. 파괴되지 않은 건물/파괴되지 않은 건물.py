def solution(board, skill):
    col = len(board[0])
    row = len(board)
    prefix = [[0]*(col+1) for _ in range(row+1)]

    for s in skill:
        type, y1,x1,y2,x2,degree = s

        if type==1:
            degree*=-1

        prefix[y1][x1] += degree
        prefix[y1][x2+1] += (degree*-1)
        prefix[y2+1][x1] += (degree*-1)
        prefix[y2+1][x2+1] += degree


    for i in range(row+1):
        for j in range(1,col+1):
            prefix[i][j]+=prefix[i][j-1]

    for i in range(col+1):
        for j in range(1,row+1):
            prefix[j][i]+=prefix[j-1][i]


    answer=0
    for i in range(row):
        for j in range(col):
            board[i][j]+=prefix[i][j]
            if board[i][j]>0:
                answer+=1
    return answer