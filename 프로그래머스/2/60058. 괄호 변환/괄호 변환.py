

def solution(p):

    if p == '':
        return ''

    u,v = split_bracket(p)
    perfect = check_perfect(u)

    if perfect:
        result = solution(v)
        answer = u+result
    else:
        result = solution(v)
        result = '('+result +')'
        arr=list(u[1:-1])

        for i in range(len(arr)):
            if arr[i] == '(':
                arr[i] = ')'
            elif arr[i] == ')':
                arr[i] = '('
        u= ''.join(arr)


        answer = result+u


    return answer

def check_perfect(u):
    stack = []
    if u[0] == ')':
        return False

    stack.append(u[0])
    for i in range(1,len(u)):
        if stack[-1] == u[i]:
            stack.append(u[i])
        else:
            stack.pop()

    if len(stack)>0:
        return False
    else:
        return True


def split_bracket(p):
    stack = []
    l_bracket = 0
    r_bracket = 0

    for i in p:
        if i == '(':
            l_bracket += 1
            stack.append(i)
        else:
            r_bracket += 1
            stack.append(i)

        if l_bracket == r_bracket:
            break
    return p[:len(stack)], p[len(stack):]

