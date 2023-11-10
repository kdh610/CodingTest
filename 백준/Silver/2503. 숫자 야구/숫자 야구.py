import sys


n=int(input())

number = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

answer = 0


for i in range(123,988):
    target = list(str(i))
    possible = True

    if len(set(str(i)))==3 and '0' not in target:
        for n,s,b in number:
            strike = 0
            ball = 0
            n = list(str(n))
            if target[0]==n[0]:
                strike+=1
            elif n[0] in target:
                ball+=1

            if target[1] == n[1]:
                strike += 1
            elif n[1] in target:
                ball += 1

            if target[2] == n[2]:
                strike += 1
            elif n[2] in target:
                ball += 1

            if strike!=s or ball!=b:
                possible=False
                break
        if possible:
            answer+=1

print(answer)