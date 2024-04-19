from collections import *
def balance_str(str):
    dict = defaultdict(int)
    index=0
    for i in range(len(str)):
        dict[str[i]]+=1

        if dict['(']==dict[')']:
            index=i
            break
    return index

def right_str(str):
    stack = []
    for s in str:
        if not stack:
            stack.append(s)
            continue

        if s=='(':
            stack.append('(')
        else:
            if stack[-1]=='(':
                stack.pop()
    if not stack:
        return True
    else:
        return False

def solution(p):
    if p=='':
        return ''

    idx = balance_str(p)
    u = p[:idx+1]
    v = p[idx+1:]


    flag = right_str(u)
    if flag:
        u+=solution(v)
        return u
    else:
        empty ='('
        empty+=solution(v)
        empty+=')'
        u=u[1:-1]
        reverse=''
        for i in u:
            if i=='(':
                reverse+=')'
            else:
                reverse+='('
        empty+=reverse
        return empty