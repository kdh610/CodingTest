def solution(n, times):
    answer = int(1e18)
    times.sort()
    start = 1
    end = n* times[-1]

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        #print('mid',mid)

        for t in times:
            cnt += mid // t

        #print(cnt)

        if cnt >= n:
            end = mid - 1
            answer = min(answer, mid)
        elif cnt < n:
            start = mid + 1

    return answer