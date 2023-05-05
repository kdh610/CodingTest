def solution(stones, k):
    answer = 0
    
    left=1
    right = int(2e9)
    
    while left<=right:
        mid = (left+right)//2

        cnt=0
        for i in range(len(stones)):
            if stones[i] - mid<0:
                cnt+=1
                if cnt==k:
                    print(cnt)
                    break
            else:
                cnt=0
        if cnt==k:
            right=mid-1
        else:
            answer=mid
            left=mid+1
            
    
    
    return answer