def solution(board):
    o=0
    x=0

    answer=1

    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                o+=1
            elif board[i][j]=='X':
                x+=1

    # 선공 여부
    if x>o:
        answer=0

    # 연속턴 여부
    if abs(o-x)>=2:
        answer=0

    # 승리 후 진행 여부
    o_win = False
    x_win = False
    # 가로
    for row in board:
        if row=="OOO":
            o_win=True
        elif row=="XXX":
            x_win=True

    # print(*list(zip(*board)), sep='\n')
    # 세로
    for row in list(zip(*board)):
        if ''.join(row) == "OOO":
            o_win = True
        elif ''.join(row) == "XXX":
            x_win = True


    # 대각
    if board[0][0]=='O' and (board[0][0]==board[1][1]==board[2][2]):
        o_win=True
    if board[0][2]=='O' and (board[0][2]==board[1][1]==board[2][0]):
        o_win=True
    if board[0][0]=='X' and (board[0][0]==board[1][1]==board[2][2]):
        x_win=True
    if board[0][2]=='X' and (board[0][2]==board[1][1]==board[2][0]):
        x_win=True

    if o_win and not x_win and o - x != 1:
        answer = 0
    elif x_win and not o_win and o != x:
        answer = 0
    elif o_win and x_win:
        answer = 0
    elif o-x>1:
        answer=0


        
    
        
    return answer