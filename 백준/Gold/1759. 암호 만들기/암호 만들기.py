from itertools import *

L, C = map(int,input().split())

password = list(input().split())

answer=[]
aeiou = ['a','e','i','o','u']
moeum = []
jaeum = []

for i in password:
    if i in aeiou:
        moeum.append(i)
    else:
        jaeum.append(i)

if len(jaeum)<2 or len(moeum)<1:
    exit()

moeum.sort()
jaeum.sort()


for i in range(1,len(moeum)+1):
    if L-i >=2:
        mo_comb = list(combinations(moeum,i))
        ja_comb = list(combinations(jaeum,L-i))

        result =list(product(mo_comb,ja_comb))

        for i in result:
            a,b = i
            temp=''.join(sorted(a+b))
            answer.append(temp)

answer.sort()

for i in answer:
    print(i)