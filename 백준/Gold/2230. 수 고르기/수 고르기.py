import sys
n,m = map(int,input().split())

arr=[int(sys.stdin.readline()) for _ in range(n)]



arr.sort()
left, right = 0,0


ans = int(2e9)+1

while left<=right and right<=n:

    dif = arr[right] - arr[left]

    if dif<m:
        right+=1
        if right>=n:
            break
    else:
        left+=1
        ans = min(ans,dif)

if m ==0:
    print(0)
else:
    print(ans)
