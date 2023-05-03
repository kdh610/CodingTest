def solution(n, lost, reserve):
    answer = n
    # 여별이 있는데 도난당했을 경우 제외
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_lost:
        print(i)
        if i - 1 in set_reserve:
            set_reserve.remove(i - 1)
        elif i + 1 in set_reserve:
            set_reserve.remove(i + 1)
        else:
            answer -= 1

    print(answer)
    return answer