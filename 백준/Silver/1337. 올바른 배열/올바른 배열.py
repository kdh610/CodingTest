

n = int(input())

arr = [int(input()) for _ in range(n)]


arr.sort()

start = 0
end = 0

answer = int(1e9)
while start<=end :



    if arr[end]-arr[start]<=4:
        answer = min(answer,5-len(arr[start:end+1]))
        if end<n-1:
            end+=1
        else:
            start+=1
    elif arr[end]-arr[start]>4:
        start+=1


print(answer)