
n = int(input())
answer = n

for i in range(1,n+1):
    result=i
    m = str(i)
    for j in m:
        result += int(j)

    if result == n:
        answer = min(answer,i)
        break

if answer==n:
    print(0)
else:
    print(answer)
