
N = int(input())

arr = list(str(N))
arr.sort(reverse=True)
print(*arr,sep="")