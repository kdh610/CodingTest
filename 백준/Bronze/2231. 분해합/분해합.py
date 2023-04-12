

n = int(input())
answer = 0

for i in range(1,n+1):
    result=i
    m = str(i)
    for j in m:
        result += int(j)

    if result == n:
        answer = i
        break


print(answer)
