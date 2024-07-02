

bar = list(input())



stack = []
answer = 0

isLaser = False
for i in range(len(bar)):
    if isLaser:
        isLaser=False
        continue

    if bar[i]=='(' and bar[i+1]==')':
        isLaser = True
        answer += len(stack)

    elif bar[i]=='(':
        stack.append('(')
    elif bar[i]==')':
        stack.pop()

        answer+=1

print(answer)