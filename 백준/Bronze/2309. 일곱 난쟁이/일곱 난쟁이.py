arr = []

for _ in range(9):
    arr.append(int(input()))

answer =[]
for i in range(9):
    result = []
    for j in range(i + 1, 9):
        for k in range(9):
            if k == i or k == j:
                continue
            result.append(arr[k])
        # print(result)
        if len(result) == 7 and sum(result) == 100:
            answer = result
            break
        result.clear()
    if len(result) == 7 and sum(result) == 100:
        break

print(*sorted(answer),sep='\n')
