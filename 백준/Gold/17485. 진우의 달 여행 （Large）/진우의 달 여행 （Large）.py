



n,m = map(int, input().split())

space = [list(map(int,input().split())) for _ in range(n)]
space.append([0]*(m))

from_left = [[int(1e9)]*(m) for _ in range(n+1)]
from_center = [[int(1e9)]*(m) for _ in range(n+1)]
from_right = [[int(1e9)]*(m) for _ in range(n+1)]


from_left[0] = space[0]
from_center[0] = space[0]
from_right[0] =  space[0]



for i in range(1,n+1):
    for j in range(m):
        if j==0:
            from_center[i][j] = min(from_left[i - 1][j], from_right[i - 1][j]) + space[i][j]
            from_right[i][j] = min(from_left[i - 1][j + 1], from_center[i - 1][j + 1]) + space[i][j]
        elif j==m-1:
            from_left[i][j] = min(from_right[i-1][j-1], from_center[i-1][j-1]) + space[i][j]
            from_center[i][j] = min(from_left[i - 1][j],from_right[i - 1][j]) + space[i][j]
        else:
            from_left[i][j] = min(from_right[i - 1][j - 1], from_center[i - 1][j - 1]) + space[i][j]
            from_center[i][j] = min(from_left[i - 1][j], from_right[i - 1][j]) + space[i][j]
            from_right[i][j] = min(from_left[i - 1][j + 1], from_center[i - 1][j + 1]) + space[i][j]


print(min( min(from_left[n]), min(from_center[n]), min(from_right[n])))

