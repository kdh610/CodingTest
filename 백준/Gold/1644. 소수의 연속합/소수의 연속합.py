import math

n = int(input())
arr = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if arr[i] == True:
        j=2
        while i*j<=n:
            arr[i*j]=False
            j+=1

prime = []
for i in range(2,n+1):
    if arr[i]==True:
        prime.append(i)

left, right = 0,1
cnt =0
if len(prime)>=1:
    sum = prime[0]


while left<=right and right<=len(prime):
    if sum==n:
        cnt+=1
        sum -= prime[left]
        left+=1
    elif sum<n:
        if right>=len(prime):
            break
        sum+=prime[right]
        right += 1
    elif sum>n:
        sum-=prime[left]
        left+=1

print(cnt)