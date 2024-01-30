def solution(msg):
    answer = []
    index = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
             'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
             'Z': 26}

    start=0
    end=1
    last=27
    result=''

    while end < len(msg)+1:
        w = msg[start:end]


        if w in index:
            result =w
            end+=1
        else:
            index[w] = last
            last+=1
            start=end-1
            end=start+1
            answer.append(index[result])
    answer.append(index[result])

    return answer