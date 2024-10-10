import math
def solution(N, stations, W):
    antenas=[]
    Range = W*2 +1
    answer = 0
    for i in stations:
        s = i-W
        e = i+W
        if s<1:
            s=1
        if e>N:
            e=N
        antenas.append((s,e))
    # print(antenas)

    district = [(0,0)]
    if not antenas:
        antenas.append((0,0))
    start = antenas[0][0]
    end = antenas[0][1]

    for i in range(len(antenas)):
        cur = antenas[i]

        if cur[0] <= end+1:
            end = cur[1]
        else:
            district.append((start,end))
            start = cur[0]
            end=cur[1]

        if i==len(antenas)-1:
            end = cur[1]
            district.append((start, end))
    district.append((N+1,N+1))

    # print(district)


    for i in range(1,len(district)):
        s1, e1 = district[i-1]
        s2, e2 = district[i]

        size = s2 - e1 - 1
        if size>0:
            if size<= Range:
                answer+=1
            else:
                answer += math.ceil(size/Range)
       


    return answer