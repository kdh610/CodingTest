s = input()

start = s[0]
zero=0
one =0
if start == '0':
    zero += 1
else:
    one += 1

for i in range(1,len(s)):
    if s[i] != start:
        if s[i]=='0':
            zero+=1
        else:
            one+=1
        start = s[i]

print(min(zero,one))