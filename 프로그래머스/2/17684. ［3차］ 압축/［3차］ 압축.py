def solution(msg):
    dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    last=26
    length = 0
    answer = []
    start = 0
    end = 1

    while start<len(msg):
        idx=0

        while True:
            w = msg[start:end]
            if w=='':
                break
            if w not in dict:
                last+=1
                dict[w]=last

                break

            idx = dict[w]

            end+=1
            if end>len(msg):
                break

        if idx!=0:
            answer.append(idx)

        start = end-1
    return answer