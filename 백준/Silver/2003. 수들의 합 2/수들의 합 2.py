

n,m = map(int,input().split())

arr = list(map(int,input().split()))

left, right =0,1

sum = arr[left]
cnt = 0

while left<= right and right<=n:

    if sum==m:
        cnt+=1
        sum -= arr[left]
        left+=1
    elif sum < m:
        if right>=n:
            break
        sum += arr[right]
        right +=1

    elif sum>m:
        sum -= arr[left]
        left +=1

print(cnt)






