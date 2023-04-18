import math

n = int(input())

prime = [True]*(n+1)

for i in range(2,int(math.sqrt(n))+1):
    if prime[i]==True:
        j=2
        while i*j<=n:
            prime[i*j]=False
            j+=1


s,e=2,2
sum = 0
cnt = 0

for i in range(2,n+1):
    if prime[i]==True:
        while sum<n and e<n+1:
            if prime[e]==True:

                sum+=e

            e += 1

        if sum==n:
            cnt+=1




        sum-=i




print(cnt)