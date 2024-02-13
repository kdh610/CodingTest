from itertools import *

N = int(input())
alpha = set()
words=''
numbers =[ str(i) for i in range(10)]


for i in range(N):
    word = input()

    if i<N-1:
        words+=word+"+"
    else:
        words+=word

    alpha.update(list(word))


alpha = list(alpha)

answer = 0
for perm in permutations(numbers,len(alpha)):
    new_words =words
    result=0
    for i in range(len(alpha)):
        new_words = new_words.replace(alpha[i],perm[i])
    for i in new_words.split('+'):
        if i.isdigit():
            result+=int(i)

    answer=max(answer, result)

print(answer)