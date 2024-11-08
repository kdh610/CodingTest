def solution(n, computers):
    
    def find(parent, x):
        if parent[x]!=x:
            parent[x] = find(parent,parent[x])
        return parent[x]

    def union(a,b, parent):
        a = find(parent,a)
        b = find(parent,b)

        if a==b:
            return False

        if a<b:
            parent[b] = a
        else:
            parent[a] = b
        return True

    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                union(i,j,parent)

    for i in range(n):
        find(parent,i)
    answer = set(parent)

    return len(answer)















