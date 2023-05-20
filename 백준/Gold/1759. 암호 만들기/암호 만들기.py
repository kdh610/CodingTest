from itertools import *

L, C = map(int,input().split())

password = list(input().split())

answer=[]
aeiou = ['a','e','i','o','u']
moeum = []
jaeum = []

# 자음, 모음 분리
for i in password:
    if i in aeiou:
        moeum.append(i)
    else:
        jaeum.append(i)

# 문제 조건이 최소 모음 1개, 최소 자음 2개여서 조건 안맞으면 종료
if len(jaeum)<2 or len(moeum)<1:
    exit()

moeum.sort()
jaeum.sort()


for i in range(1,len(moeum)+1):
    # 모음 2개이상 조합 가능한 경우만
    if L-i >=2:
        mo_comb = list(combinations(moeum,i))
        ja_comb = list(combinations(jaeum,L-i))

        result =list(product(mo_comb,ja_comb))

        for i in result:
            # result 결과가 튜플로 나와서 튜플을 합치고 정렬
            a,b = i
            # 문자들 합쳐서 문자열로 만들기
            temp=''.join(sorted(a+b))
            answer.append(temp)

answer.sort()

for i in answer:
    print(i)
