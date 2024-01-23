def solution(n, arr1, arr2):
    answer = []
    result =[]
    
    for i in range(n):
        temp=''
        result.append(arr1[i]|arr2[i])

        for j in format(result[i],'b').zfill(n):
            if j=='1':
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
        
    
    return answer