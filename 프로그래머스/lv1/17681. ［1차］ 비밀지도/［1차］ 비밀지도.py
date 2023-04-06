def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        first = int(arr1[i])
        second = int(arr2[i])
        result = bin(first | second)[2:]
        while len(result)<n:
            result = "0"+result
        answer.append(result)


    for j,row in enumerate(answer):
        temp = ""
        for i,v in enumerate(row):
            if v=="1":
                temp+="#"
            elif v=="0":
                temp+=" "
        answer[j] = temp

    return answer