
def solution(stones, k):
    start = 1
    end = int(2e9)
    answer = 0
    while start<=end:
        #max_len = 0
        mid = (start+end)//2
        cnt=0

        for i in range(len(stones)):

            if stones[i] < mid:

                cnt+=1
                #max_len= max(max_len,cnt)
                if cnt==k:
                    break
            else:
                cnt=0

        if cnt==k:
            end = mid-1
        else:
            start = mid+1
            answer= mid
    
    return answer