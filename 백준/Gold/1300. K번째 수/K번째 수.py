
n = int(input())
k = int(input())

answer = n**2
left = 0
right = n**2

# k번째 수는 그 수보다 작은 수가 k-1개 있다는 의미
while left <= right:
    mid = (left+right)//2
    cnt = 0
    #각행 마다 mid보다 작은 수 갯수 카운트
    for i in range(1,n+1):
        cnt += min(mid // i, n)

    if cnt < k:
        left = mid+1
    else:
        right = mid-1
        answer = min(answer,mid)

print(answer)




