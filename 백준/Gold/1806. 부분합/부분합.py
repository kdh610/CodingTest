
n,s = map(int,input().split())
arr = list(map(int,input().split()))

left, right = 0,1
sum = arr[0]
ans = len(arr)
possible = False

while left<=right :
    if sum<s:
        if right>=n:
            break
        sum+=arr[right]
        right+=1

    elif sum>=s:
        possible = True
        ans = min(ans,right-left)
        sum-=arr[left]
        left+=1

if possible:
    print(ans)
else:
    print(0)