
import re

answer=''
board = input()

p = re.compile('X*')

x = p.findall(board)



for i in range(len(x)-1):
    if len(x[i])%2==1:
        answer=-1
        break
    if len(x[i])==2:
        answer += 'BB'
    elif x[i]=='':
        answer +='.'
    else:
        for j in range(0,len(x[i]),4):
            if len(x[i][j:j+4])==4:
                answer += 'AAAA'
            else:
                answer += 'BB'

print(answer)

