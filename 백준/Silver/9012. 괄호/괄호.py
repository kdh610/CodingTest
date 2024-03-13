
T = int(input())

for _ in range(T):
    bracket = input()
    stack = []

    for i in bracket:
        if i=='(':
            stack.append(i)

        else:
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        print('NO')
    else:
        print('YES')