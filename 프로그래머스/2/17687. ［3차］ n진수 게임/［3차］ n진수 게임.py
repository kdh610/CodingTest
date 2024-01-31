
def convert_format(n, x):
    result = ''
    while True:
        q,r = divmod(x,n)
        x=q

        if r==10:
            r = 'A'
        elif r==11:
            r='B'
        elif r==12:
            r='C'
        elif r==13:
            r='D'
        elif r==14:
            r='E'
        elif r==15:
            r='F'

        result=str(r) +result
        if x==0:
            break
    return result

def solution(n, t, m, p):
    number = 0
    numbers=''
    answer=''
    while len(numbers)<=t*m:
        numbers+=convert_format(n,number)
        number+=1


    print(numbers)
    for i in range(len(numbers)):
        answer+=numbers[(p+m*i)-1]

        if len(answer)==t:
            break
    return answer