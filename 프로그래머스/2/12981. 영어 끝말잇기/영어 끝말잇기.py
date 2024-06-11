def solution(n, words):
    prev = words[0]
    person = 0

    used = set()
    used.add(prev)
    for idx, word in enumerate(words[1:]):
        if prev[-1] != word[0]:
            person = idx+2
            break
        if word in used:
            person = idx+2
            break
        used.add(word)
        prev = word

    num,order =0,0

    if person!=0:
        num = person % n
        if num ==0:
            num = n

        order = person // n +1
        if person%n == 0:
            order -= 1



    print([num, order])

    return [num, order]