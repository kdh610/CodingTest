def solution(s):
    s=list(s)
    s.sort(reverse = True)
    print(s)
    s = ''.join(s)
    return s