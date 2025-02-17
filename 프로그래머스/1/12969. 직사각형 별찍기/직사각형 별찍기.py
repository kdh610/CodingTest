a, b = map(int, input().strip().split(' '))

answer = [ ['*']*a for _ in range(b)]

for i in range(b):
    print(a*'*')
