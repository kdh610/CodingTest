def solution(people, limit):
    people.sort()

    n = len(people)
    cnt = 0
    start = 0
    end = n-1
    answer = 0
    temp = []
    while start <= end:
        if people[start] + people[end] <= limit:
            cnt += 2
            start += 1
            end -= 1
            answer += 1
        else:
            temp.append(people[end])
            end -= 1

    return answer+len(temp)