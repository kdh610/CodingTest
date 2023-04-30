

G = int(input())

start, end =1,1


answer = []
while True:
    if end-start==1 and (end**2 - start**2) >G:
        break

    if (end**2 - start**2) == G:
        answer.append(end)

    if (end**2 - start**2) <=G:
        end+=1
    else:
        start+=1


if len(answer)>0:
    for i in answer:
        print(i)
else:
    print(-1)