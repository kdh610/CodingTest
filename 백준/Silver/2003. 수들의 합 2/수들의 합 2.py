n,m = map(int,input().split())
arr = list(map(int,input().split()))

left, right = 0,0
sum = arr[0]
ans = 0

while True:
    try:
        if sum == m:
            ans+=1
            sum-=arr[left]
            left+=1
            
        elif sum < m:
            right+=1
            sum+=arr[right]
        elif sum > m:
            sum -= arr[left]
            left +=1
    except:
        break


print(ans)



