from collections import *
import copy
def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    def check_block(y,x):
        check_remove = False
        target = board[y][x]
        if 0<= x+1 <n and 0<=y+1<m:
            if target == board[y+1][x+1] and target==board[y][x+1] and target==board[y+1][x]:
                #print(y,x)
                temp_board[y][x]='*'
                temp_board[y+1][x] = '*'
                temp_board[y][x+1] = '*'
                temp_board[y+1][x+1] = '*'
                remove.add((y,x))
                remove.add((y, x+1))
                remove.add((y+1, x))
                remove.add((y+1, x+1))
                check_remove =True
        #print(*temp_board,sep='\n')
        return check_remove

    def block_down(temp_board):
        for i in range(m-1,-1,-1):
            for j in range(n):
                if temp_board[i][j] !='*':
                    Q=deque()
                    Q.append((i,j))
                    while Q:
                        y,x = Q.popleft()
                        if 0<=y+1<m and temp_board[y+1][j]=='*':
                            temp_board[y][x], temp_board[y+1][x] = temp_board[y+1][x], temp_board[y][x]
                            Q.append((y+1,x))
        #print(*temp_board,sep='\n')
        #print('')

    temp_board = copy.deepcopy(board)
    while True:
        #4개짜리 블록찾기
        check_remove = False
        remove = set()
        for i in range(m):
            for j in range(n):
                if board[i][j]!='*':
                    check = check_block(i,j)
                    if check: check_remove=True
        #print(*temp_board,sep='\n')
        #print(remove)
        #print(' ')
        answer += len(remove)
        #종료 조건 더이상 터진 블록이 없을 때
        if not check_remove:
            break

        #블럭 내려오기
        block_down(temp_board)
        board = copy.deepcopy(temp_board)

    return answer