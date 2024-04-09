from collections import *
def solution(board, moves):
    N=len(board)
    answer = 0
    stack = []
    for col in moves:
        col -=1
        target=0
        for i in range(N):
            if board[i][col]!=0:
                target = board[i][col]
                board[i][col] = 0
                break
        
        if target!=0:
        
            if len(stack)==0: stack.append(target)
            else:
                if stack[-1] == target:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(target)
                
    return answer

