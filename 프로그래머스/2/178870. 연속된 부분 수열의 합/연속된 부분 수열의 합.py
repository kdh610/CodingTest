def solution(sequence, k):
    answer = []
    left, right =0,0
    sequence.sort()
    hap = sequence[left]
    length = int(1e6)+1
    al, ar = 0,0
    while left<=right:

        # hap = sum(sequence[left:right+1])
        # print('left,right',left,right)
        # print(hap)
        if hap==k:
            if right-left+1<length:
                al,ar=left,right
                length=right-left+1
            elif right-left+1==length and left<al:
                al,ar=left,right

        if hap<k and right<len(sequence)-1:

            right+=1
            hap+=sequence[right]

        else:
            hap-=sequence[left]
            left+=1


    answer = [al,ar]
    return answer